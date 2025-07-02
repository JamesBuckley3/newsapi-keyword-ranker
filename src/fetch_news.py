import requests
import time
from datetime import date, timedelta

# Your NewsAPI key
API_KEY = "your_api_key_here"

# Base URL for fetching news articles
BASE_URL = "https://newsapi.org/v2/everything"

# Topics to search for in the news (limit of 100)
TOPICS = ["technology", "climate", "economy", "politics", "health", "sports"]

# Fetch news from yesterday (not today) to ensure more than 0 results
YESTERDAY = (date.today() - timedelta(days=1)).isoformat()


def fetch_top_headlines():
    """
    Fetches top news articles for each topic from NewsAPI's 'everything' endpoint,
    filtered by language, topic keyword, and date (yesterday).

    Returns:
        list: Combined list of all articles fetched across all topics
    """
    all_articles = []

    for topic in TOPICS:
        print(f"Fetching news for topic: {topic.upper()}")

        # Construct the API request URL
        url = (
            f"{BASE_URL}?q={topic}"
            f"&language=en"
            f"&from={YESTERDAY}"
            f"&sortBy=publishedAt"
            f"&pageSize=100"
            f"&page=1"
            f"&apiKey={API_KEY}"
        )

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                articles = data.get("articles", [])
                print(f"Retrieved {len(articles)} articles for '{topic}'")
                all_articles.extend(articles)
            else:
                print(f"API error {response.status_code} for topic '{topic}'")

        except Exception as e:
            print(f"Request failed for topic '{topic}': {e}")

        time.sleep(1)  # Pause to avoid rate-limiting

    return all_articles
