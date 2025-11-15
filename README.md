***🚀 Threads Keyword Scraper + Embedding Visualization (GCP Integrated)***

This project is a Python-based system for scraping Threads posts by keyword, storing them in Google Cloud Storage, and visualizing embeddings using PCA + UMAP for cluster inspection and qualitative analysis.

It is designed for reliability, human-like browser automation, anti-detection behavior, and seamless integration with GCP.

***✨ Key Features***<br />
<br />

***☁️ Google Cloud Integration***<br />
<br />
Automatically uploads scraped data to a Google Cloud Storage (GCS) bucket in .jsonl format, with filenames including both the keyword and date:

jpn/threads_{keyword}_{date}.jsonl<br />
<br />

***🛡️ Anti-Detection Scraping***

Built to minimize the risk of automated scraping detection:

Randomized User-Agent pool

Disabled Selenium automation flags

Suppression of navigator.webdriver

Random viewport sizes

Natural mouse movement + interaction timing
&nbsp;
&nbsp;
***🤖 Human-Like Interaction***

The scraper simulates real user behavior:

Randomized delays between navigation, typing, and clicking

Character-by-character typing with variable speed

Natural scrolling patterns with pauses to mimic reading behavior<br />
<br />

***🎯 Targeted Keyword Scraping***

Scrapes posts for a customizable list of keywords, such as:

韓国, Kポ, 韓国旅行, K-POP, 韓国ドラマ, など


For each keyword:

Searches Threads

Scrolls and loads content

Captures up to TARGET_POSTS_NUM posts (default = 100)<br />
<br />

***🛠️ Robust Scraping Pipeline***

Selenium handles browser automation

BeautifulSoup parses DOM content

HTML is processed to extract text reliably

Each post is saved as a structured JSON object:

{
    "id": "<hashed-unique-id>",
    "genre": "<keyword>",
    "content": "<scraped text>",
    "acquired_at": "<timestamp>",
    "in_out": "<category>"
}<br />
<br />

***📊 NEW: Embedding Visualization Pipeline (PCA + UMAP)***

This repo now includes a full embedding visualization pipeline (visualization_emb.py) that:

Loads embeddings from BigQuery

Runs PCA for initial reduction

Applies UMAP for high-quality 2D visualization

Produces scatterplots for:

cluster separation

outlier detection

qualitative comparison

model version drift analysis

Useful for understanding:

semantic similarity

how keywords cluster

model embedding quality over time<br />
<br />

***✅ Prerequisites***

You will need:

Python 3.x

A Google Cloud Platform (GCP) project

A GCS bucket

A Google Service Account JSON credentials file

A working Threads account (for scraping)<br />
<br />

***⚙️ Installation***

Clone the repository:

git clone https://github.com/kimarkim/threads_GCP.git
cd threads_GCP


Install dependencies:

pip install -r requirements.txt


Included packages:

functions-framework

google-cloud-storage

selenium

beautifulsoup4

umap-learn

scikit-learn

numpy<br />
<br />

***📝 Configuration***

Create a .env file in the root of the project:

THREADS_USERNAME="your_threads_username"
THREADS_PASSWORD="your_threads_password"
BUCKET_NAME="your_gcs_bucket_name"
GCP_CREDENTIALS="/path/to/your/gcp-credentials.json"


(For visualization: BigQuery config is handled in the script.)

▶️ Usage
1. Run the Scraper
python main.py


The scraper will:

Log in to Threads

Loop through TARGET_KEYWORD

Scrape up to TARGET_POSTS_NUM posts

Upload a .jsonl file to your GCS bucket

Close the session

2. Run the Embedding Visualization
python visualization_emb.py


This will:

Query embeddings from BigQuery

Perform PCA + UMAP

Generate plots

Optionally save visualization outputs<br />
<br />

***📁 Project Structure***
threads_GCP/
 ├── main.py                # Scraper logic
 ├── visualization_emb.py   # PCA+UMAP visualization pipeline
 ├── requirements.txt       # Python dependencies
 ├── README.md              # Project documentation
 ├── utils/                 # Helper modules
 └── data/                  # Temporary storage / artifacts<br />
<br />

***📄 License***

This project is licensed under the Apache License 2.0.
See the LICENSE file for details.<br />
<br />
***⚠️ Disclaimer***

This tool is intended for educational and research purposes.
Please:

Respect the Terms of Service of Threads

Avoid aggressive scraping patterns

Do not misuse the tool

The author assumes no responsibility for improper or unethical usage.
