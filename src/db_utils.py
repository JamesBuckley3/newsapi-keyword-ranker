import psycopg2
from datetime import date

# Database connection parameters
DB_PARAMS = {
    "dbname": "newsapi_pipeline",
    "user": "your_username",
    "password": "your_password",
    "host": "localhost",
    "port": 5432,
}


def get_connection():
    """
    Establishes and returns a connection to the PostgreSQL database.
    """
    return psycopg2.connect(**DB_PARAMS)


def get_or_create_source(conn, source_dict):
    """
    Retrieves a source ID if the source already exists, or inserts a new one.

    Args:
        conn (psycopg2.connection): Active database connection
        source_dict (dict): Source info from the article (contains 'name' and optionally 'url')

    Returns:
        int: ID of the existing or newly inserted source
    """
    name = source_dict.get("name")
    url = source_dict.get("url", "")

    with conn.cursor() as cur:
        # Check if source already exists
        cur.execute("SELECT id FROM sources WHERE name = %s", (name,))
        result = cur.fetchone()
        if result:
            return result[0]

        # Insert new source
        cur.execute(
            "INSERT INTO sources (name, url) VALUES (%s, %s) RETURNING id", (name, url)
        )
        return cur.fetchone()[0]


def save_keyword_ranking(conn, keyword, count, rank):
    """
    Inserts a keyword ranking into the database.

    Args:
        conn (psycopg2.connection): Active database connection
        keyword (str): The keyword text
        count (int): Frequency count of the keyword
        rank (int): Rank position (1 = most frequent)
    """
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO keyword_rankings (keyword, count, rank, collected_at)
                VALUES (%s, %s, %s, %s)
                """,
                (keyword, count, rank, date.today()),
            )
    except Exception as e:
        print(f"Failed to save keyword '{keyword}': {e}")


def save_article(conn, article):
    """
    Inserts a news article into the database. Also ensures its source is stored.

    Args:
        conn (psycopg2.connection): Active database connection
        article (dict): Article data from NewsAPI
    """
    source_info = article.get("source", {})
    source_id = get_or_create_source(conn, source_info)

    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO articles (title, author, description, url, published_at, source_id)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (url) DO NOTHING
                """,
                (
                    article.get("title"),
                    article.get("author"),
                    article.get("description"),
                    article.get("url"),
                    article.get("publishedAt"),
                    source_id,
                ),
            )
    except Exception as e:
        print(f"Failed to insert article: {e}")
