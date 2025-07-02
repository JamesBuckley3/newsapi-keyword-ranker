import re
from collections import Counter
import nltk
from nltk.corpus import stopwords

# Download English stopwords on first run
nltk.download("stopwords")


def extract_keywords_from_titles(titles, dynamic_stopwords=None, top_n=20):
    """
    Extracts the most common keywords from a list of article titles.

    Args:
        titles (list): List of article title strings
        dynamic_stopwords (set): Optional extra stopwords (e.g. source fragments)
        top_n (int): Number of top keywords to return

    Returns:
        list: Top `n` keywords as (keyword, count) tuples
    """
    # Load standard English stopwords from NLTK
    stop_words = set(stopwords.words("english"))

    # Add custom project-specific stopwords you don't want for charting/analysis
    custom = {
        "says",
        "report",
        "us",
        "uk",
        "new",
        "get",
        "news",
        "first",
        "2025",
        "top",
    }
    stop_words.update(custom)

    # Add dynamic stopwords from source names if provided
    if dynamic_stopwords:
        stop_words.update(dynamic_stopwords)

    keywords = []

    for title in titles:
        words = re.findall(r"\b\w+\b", title.lower())
        filtered = [w for w in words if w not in stop_words and len(w) > 2]
        keywords.extend(filtered)

    return Counter(keywords).most_common(top_n)


def build_source_stopwords(articles):
    """
    Extracts word fragments from article source names to avoid including them as keywords.

    Args:
        articles (list): List of article dictionaries

    Returns:
        set: Word fragments found in all source names (e.g. "bbc", "cnn")
    """
    fragments = set()

    for article in articles:
        source = article.get("source", {}).get("name", "").lower()
        if source:
            words = re.findall(r"\b\w+\b", source)
            fragments.update(words)

    return fragments
