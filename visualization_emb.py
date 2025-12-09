import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import umap
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Hiragino Sans"
from google.cloud import bigquery
from dotenv import load_dotenv
import hdbscan   
import os


## Load Credentials
load_dotenv()

PROJECT_ID = os.environ.get("PROJECT_ID")
DATASET = os.environ.get("DATASET")
TABLE = os.environ.get("TABLE")

client = bigquery.Client(project=PROJECT_ID)

query = f"""
SELECT
  id,
  post,
  genre,
  embeddings,
FROM `{PROJECT_ID}.{DATASET}.{TABLE}`
LIMIT 5000
"""

df = client.query(query).to_dataframe()
df.head(3)


X = np.vstack(df["embeddings"].values)

pca = PCA(n_components=45, random_state=42)
X_pca = pca.fit_transform(X)

# HDBSCAN on PCA space
clusterer = hdbscan.HDBSCAN(min_cluster_size=8, min_samples=3, metric="euclidean")
df["cluster"] = clusterer.fit_predict(X_pca)


reducer = umap.UMAP(
    n_components=2,
    n_neighbors=20,
    min_dist=0.1,
    random_state=42
)
X_2d = reducer.fit_transform(X_pca)

df["x"] = X_2d[:, 0]
df["y"] = X_2d[:, 1]


# cluster plot
plt.figure(figsize=(10, 7))
unique_clusters = np.sort(df["cluster"].unique())
for cid in unique_clusters:
    mask = df["cluster"] == cid
    label = "noise (-1)" if cid == -1 else f"cluster {cid}"
    plt.scatter(df.loc[mask, "x"], df.loc[mask, "y"], s=8, alpha=0.7, label=label)
plt.legend(markerscale=2)
plt.title("Threads Post Embeddings — HDBSCAN Clusters")
plt.xlabel("UMAP-1")
plt.ylabel("UMAP-2")
plt.show()