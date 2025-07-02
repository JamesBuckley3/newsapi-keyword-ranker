from datetime import date
from fetch_news import fetch_top_headlines
from keyword_extractor import extract_keywords_from_titles, build_source_stopwords
from visualise_keywords import fetch_keywords, plot_keywords
from db_utils import get_connection, save_article, save_keyword_ranking


def run_keyword_pipeline():
    """
    Runs the full daily keyword ranking pipeline:
    1. Connects to the PostgreSQL database
    2. Fetches top news articles via NewsAPI
    3. Saves articles and their sources to the database
    4. Extracts keywords from titles and ranks them
    5. Stores the top keywords in the database
    6. Generates a bar chart of the top keywords
    7. Commits changes and closes the connection
    """

    conn = get_connection()
    print("🔌 Connected to database.")

    articles = fetch_top_headlines()
    print(f"📰 Fetched {len(articles)} total articles")

    for article in articles:
        try:
            save_article(conn, article)
        except Exception as e:
            print(f"❌ Failed to save article: {e}")

    titles = [a["title"] for a in articles if a.get("title")]
    source_stopwords = build_source_stopwords(articles)

    top_keywords = extract_keywords_from_titles(
        titles, dynamic_stopwords=source_stopwords
    )

    for rank, (keyword, count) in enumerate(top_keywords, start=1):
        try:
            save_keyword_ranking(conn, keyword, count, rank)
        except Exception as e:
            print(f"❌ Failed to save keyword: {e}")

    target_date = date.today().isoformat()
    top_keywords_for_chart = fetch_keywords(conn, target_date, limit=10)
    plot_keywords(top_keywords_for_chart, f"charts/top_keywords_{target_date}.png")

    conn.commit()
    conn.close()
    print("✅ Pipeline finished and database changes committed.")


if __name__ == "__main__":
    run_keyword_pipeline()
