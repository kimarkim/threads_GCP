**🚀 Threads Keyword Scraper for GCP**
This project is a Python-based web scraper designed to extract posts from Threads based on a predefined list of keywords. It automates the process of logging in, searching for keywords, scrolling through results, and collecting post data. The scraped data is then processed and uploaded directly to a specified Google Cloud Storage (GCS) bucket in JSONL format.

**✨ Key Features**

**☁️ Google Cloud Integration: **
Automatically uploads scraped data to a Google Cloud Storage bucket, formatted with the keyword and scrape date (e.g., jpn/threads_{keyword}_{date}.json).

**🛡️ Advanced Anti-Detection: Implements several techniques to avoid being blocked:**

- Uses a pool of random User-Agents to mimic different browsers.

- Disables browser automation flags and hides the navigator.webdriver property.

- Sets a random browser viewport size for each session.


**🤖 Human-Like Interaction: Simulates human behavior to appear less like a bot:**

- Introduces random delays between actions like navigation, typing, and clicking.

- Types text character-by-character with randomized delays.

- Executes varied and "natural" scrolling patterns, including random pauses to simulate reading or distraction.


**🎯 Targeted Keyword Scraping:** Iterates through a list of specified keywords (韓国, Kポ, 韓国旅行, etc.) to collect relevant posts.


**🛠️ Robust Scraping Process: **Uses BeautifulSoup for parsing HTML and Selenium for browser automation to reliably extract post text.


**📄 Data Formatting: **Each post is structured into a JSON object with a unique ID (hashed from its content), genre (keyword), the post content, acquisition date, and an "in_out" field.

**✅ Prerequisites**
Before you begin, ensure you have the following:

Python 3.x

- A Google Cloud Platform (GCP) account with a project set up.

- A GCS bucket created within your GCP project.

- GCP credentials (a service account key file in JSON format).

- A Threads account.

**⚙️ Installation**
Clone the repository:

git clone [https://github.com/kimarkim/threads_gcp.git](https://github.com/kimarkim/threads_gcp.git)
cd threads_gcp

Install the required dependencies:

pip install -r requirements.txt

The necessary packages are: functions-framework, google-cloud-storage, selenium, beautifulsoup4, and numpy.

**📝 Configuration**
The script uses environment variables for configuration. Create a .env file in the root directory of the project and add the following variables:

THREADS_USERNAME="your_threads_username"
THREADS_PASSWORD="your_threads_password"
BUCKET_NAME="your_gcs_bucket_name"
GCP_CREDENTIALS="/path/to/your/gcp-credentials.json"

**▶️ Usage**
Once the installation and configuration steps are complete, you can run the scraper using the following command:

python main.py

- The script will perform the following actions:

- Log in to Threads using the provided credentials.

- For each keyword in TARGET_KEYWORD:

- Navigate to the search results page.

- Scrape up to TARGET_POSTS_NUM (default is 100) posts.

- Upload the collected data as a .jsonl file to your GCS bucket.

- Close the browser session upon completion.

📄 License
This project is licensed under the Apache License, Version 2.0. See the LICENSE file for more details.

⚠️ Disclaimer: This tool is intended for educational and data collection purposes. Please be responsible and respect the terms of service of Threads. The developers of this tool are not responsible for any misuse.
