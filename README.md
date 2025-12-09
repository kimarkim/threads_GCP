# 🚀 Threads Keyword Scraper + Embedding Visualization (GCP Enabled)
- A Python system for scraping Threads posts by keyword, storing results in Google Cloud Storage, and visualizing text embeddings using PCA + UMAP for clustering and qualitative analysis.

- Built for reliability, human-like automation, and seamless GCP integration.

# 🛠️ Tech Stack
- Python, Google Cloud Platform (GCS, BigQuery), Selenium, BeautifulSoup4, Pandas, NumPy, Scikit-learn, UMAP, HDBSCAN, Matplotlib, LangDetect, PyArrow.

# ✨ Features

**☁️ Google Cloud Storage Integration**

- Automatically uploads scraped posts to GCS as .parquet:

- jpn/threads_{keyword}_{date}.parquet

# 🛡️ Anti-Detection Scraping
- Designed to mimic real browser behavior:

- Randomized User-Agent pool

- Selenium automation flags disabled

- navigator.webdriver suppressed


**Variable viewport sizes**

Natural mouse movement and timing

# 🤖 Human-Like Interaction
- Randomized delays for navigation, typing, and clicking

- Character-by-character text entry

- Natural scrolling with pauses

# 🎯 Keyword-Based Scraping
- Scrapes posts for a customizable keyword list (e.g., 韓国, K-POP, 韓国旅行).

**For each keyword, the scraper:**

- Searches Threads

- Loads more results by scrolling

- Captures up to TARGET_POSTS_NUM posts (default: 100)

- Each post is saved as structured Parquet data with the following schema:

**{ "id": "<hashed-id>", "keyword": "<keyword>", "post": "<text>", "acquire_date": "<date>", "language": "<detected-lang>" }**

# 📊 Embedding Visualization (PCA + UMAP)
**visualization_emb.py provides a complete embedding analysis workflow:**

- Loads embeddings from BigQuery

- Applies PCA for initial dimensionality reduction

- Applies UMAP for 2D visualization

**Generates plots for:**

- Cluster structure

- Outlier detection

- Keyword similarity

- Model drift analysis

**Useful for understanding semantic patterns and monitoring embedding quality.**

# ✅ Requirements
- Python 3.x

- Google Cloud project + GCS bucket

- Service Account JSON key

- Threads account (for login)

# ⚙️ Installation
- git clone https://github.com/kimarkim/threads_GCP.git

- cd threads_GCP

- pip install -r requirements.txt

# 📝 Configuration
**Create a .env file:**

THREADS_USERNAME="your_username" THREADS_PASSWORD="your_password" BUCKET_NAME="your_gcs_bucket" GCP_CREDENTIALS="/path/to/credentials.json" PROJECT_ID="your_gcp_project_id" DATASET="your_bigquery_dataset" TABLE="your_bigquery_table"

# ▶️ Usage
**1. Run the Scraper python main.py**

This will:

- Log in to Threads

- Iterate through keywords

- Scrape posts

- Upload .parquet results to GCS

**2. Run Embedding Visualization**

- python visualization_emb.py

This will:

- Query embeddings from BigQuery

- Perform PCA + UMAP

- Generate visual plots (optional save)

# 📁 Project Structure
threads_GCP/ ├── main.py # Scraper orchestration ├── threads_scraper.py # Selenium scraper logic ├── clean_data.py # Data cleaning logic ├── visualization_emb.py # PCA + UMAP workflow ├── requirements.txt

├── README.md

# 📄 License
Apache License 2.0. See LICENSE for details.

# ⚠️ Disclaimer
This project is for research and educational use.

Please respect Threads' Terms of Service and avoid harmful or abusive scraping.
