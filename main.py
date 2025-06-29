import os
import time
import json
from google.cloud import storage
import datetime
from google.api_core import exceptions
from threads_scraper import ThreadsScraper
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
USERNAME = os.environ.get('THREADS_USERNAME')
PASSWORD = os.environ.get('THREADS_PASSWORD')
TARGET_KEYWORD = ["韓国", "Kポ", "韓国旅行","韓国ファッション","韓国コスメ","韓国グルメ","韓国語","韓国留学","韓国生活"]
TARGET_POSTS_NUM = 100
BUCKET_NAME = os.environ.get('BUCKET_NAME')

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.environ.get('GCP_CREDENTIALS')

def upload_file_gcs(storage_client, bucket_name, data, destination_file_name):
    """Upload data to Google Cloud Storage"""
    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_file_name)
        
        # Convert to JSON string (don't encode to bytes)
        jsonl_data = "\n".join(json.dumps(post, ensure_ascii=False) for post in data)
        blob.upload_from_string(jsonl_data, content_type='application/jsonl')
        print(f"Successfully uploaded to {destination_file_name}")
        return True
    except Exception as e:
        print(f"Failed to upload {destination_file_name}: {e}")
        return False

def main():
    """
    Main function to orchestrate the scraping and GCS upload process.
    """
    scraper = ThreadsScraper()

    try:
        if scraper.login_threads(USERNAME, PASSWORD):
            
            # Initializing cloud storage
            storage_client = storage.Client()

            for keyword in TARGET_KEYWORD:
                print(f"Processing keyword: {keyword}")
                
                if not scraper.redirect_url(keyword):
                    print(f"Failed to redirect for keyword: {keyword}. Skipping.")
                    continue
                
                time.sleep(2)  # Wait for page to load after redirect
                
                # Scrape posts
                scraped_posts = scraper.scrape(keyword, TARGET_POSTS_NUM)

                if not scraped_posts:
                    print(f"Failed to scrape posts for '{keyword}'. Can't upload.")
                    continue

                print(f"Found {len(scraped_posts)} posts for '{keyword}'.")

                # Upload to GCS with properly formatted filename
                scraped_date = datetime.datetime.now().strftime('%Y-%m-%d')
                destination_file_name = f'jpn/threads_{keyword}_{scraped_date}.json'

                success = upload_file_gcs(
                    storage_client, 
                    BUCKET_NAME, 
                    scraped_posts,
                    destination_file_name
                )
                
                if success:
                    print(f"✅ Successfully uploaded {len(scraped_posts)} posts for '{keyword}'.")
                else:
                    print(f"❌ Failed to upload posts for '{keyword}'.")

            scraper.close_session()

    except Exception as e:
        print(f"An unexpected error occurred in the main process: {e}")
        if 'scraper' in locals():
            scraper.close_session()

    finally:
        print("✅ Task Done ✅")

if __name__ == "__main__":
    main()