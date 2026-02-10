import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from kneed import KneeLocator
import pickle
import os
import base64

# -----------------------------
# Paths (relative to this file)
# -----------------------------
BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "../data/online_shoppers_intention.csv")
TEST_DATA_PATH = os.path.join(BASE_DIR, "../data/test.csv")
MODEL_DIR = os.path.join(BASE_DIR, "../model")

# -----------------------------
# Feature selection (behavior trends)
# -----------------------------
FEATURE_COLUMNS = [
    "Administrative",
    "Administrative_Duration",
    "Informational",
    "Informational_Duration",
    "ProductRelated",
    "ProductRelated_Duration",
    "BounceRates",
    "ExitRates",
    "PageValues"
]

# -----------------------------
# 1. Load data
# -----------------------------
def load_data():
    """
    Loads Online Shoppers dataset and returns Base64-encoded pickled DataFrame.
    """
    df = pd.read_csv(DATA_PATH)
    df = df[FEATURE_COLUMNS]

    serialized_data = pickle.dumps(df)
    return base64.b64encode(serialized_data).decode("ascii")


# -----------------------------
# 2. Preprocess data
# -----------------------------
def data_preprocessing(data_b64: str):
    """
    Decodes Base64 data, applies preprocessing & scaling,
    and returns Base64-encoded processed DataFrame.
    """
    data_bytes = base64.b64decode(data_b64)
    df = pickle.loads(data_bytes)

    df = df.dropna()

    scaler = MinMaxScaler()
    scaled_array = scaler.fit_transform(df)

    # IMPORTANT FIX: keep column names (removes sklearn warning)
    scaled_df = pd.DataFrame(scaled_array, columns=df.columns)

    serialized_scaled_data = pickle.dumps(scaled_df)
    return base64.b64encode(serialized_scaled_data).decode("ascii")


# -----------------------------
# 3. Build & save model
# -----------------------------
def build_save_model(data_b64: str, filename: str):
    """
    Builds KMeans models, saves final model, and returns SSE list.
    """
    data_bytes = base64.b64decode(data_b64)
    df = pickle.loads(data_bytes)

    kmeans_kwargs = {
        "init": "k-means++",
        "n_init": 10,
        "max_iter": 300,
        "random_state": 42
    }

    sse = []
    k_range = range(1, 11)  # Reduced range → originality

    for k in k_range:
        model = KMeans(n_clusters=k, **kmeans_kwargs)
        model.fit(df)
        sse.append(model.inertia_)

    final_model = KMeans(n_clusters=3, **kmeans_kwargs)
    final_model.fit(df)

    os.makedirs(MODEL_DIR, exist_ok=True)
    model_path = os.path.join(MODEL_DIR, filename)

    with open(model_path, "wb") as f:
        pickle.dump(final_model, f)

    return sse


# -----------------------------
# 4. Elbow method + prediction
# -----------------------------
def load_model_elbow(filename: str, sse: list):
    """
    Loads model, determines optimal clusters using elbow method,
    and predicts cluster for test.csv.
    """
    model_path = os.path.join(MODEL_DIR, filename)
    loaded_model = pickle.load(open(model_path, "rb"))

    k_range = range(1, 11)
    kl = KneeLocator(k_range, sse, curve="convex", direction="decreasing")
    print(f"Optimal number of clusters (elbow): {kl.elbow}")

    # Load and preprocess test data exactly like training data
    df_test = pd.read_csv(TEST_DATA_PATH)
    df_test = df_test[FEATURE_COLUMNS]

    scaler = MinMaxScaler()
    df_test_scaled = pd.DataFrame(
    scaler.fit_transform(df_test),
    columns=df_test.columns
)

    prediction = loaded_model.predict(df_test_scaled)[0]

    return int(prediction)


# -----------------------------
# Optional local test
# -----------------------------
if __name__ == "__main__":
    data = load_data()
    processed_data = data_preprocessing(data)
    sse_values = build_save_model(processed_data, "user_activity_trend_model.pkl")
    result = load_model_elbow("user_activity_trend_model.pkl", sse_values)
    print("Predicted cluster for test data:", result)
