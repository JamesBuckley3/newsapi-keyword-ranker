# 📰 NewsAPI Keyword Pipeline

Automatically fetches daily top-headline news articles, extracts keywords from the titles, ranks them by frequency, and stores the results in a PostgreSQL database. Each day, it generates a bar chart of the top keywords and saves it locally.

## 🔧 Features

- Fetches global news headlines from NewsAPI
- Cleans and deduplicates data
- Stores articles, sources, and keyword rankings in PostgreSQL
- Generates a daily bar chart of trending keywords
- Supports future expansion for trend tracking and analysis

## 📦 Technologies

![Python](images/python_logo.png "Python")&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![PostgreSQL](images/postgresql_logo.png "PostgreSQL")&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![DBeaver](images/dbeaver_logo.png "DBeaver")&nbsp;&nbsp;&nbsp;&nbsp;![VSCode](images/vscode_logo.png "VSCode")

- Python (requests, psycopg2, matplotlib, NLTK)
- PostgreSQL + pgAdmin
- [NewsAPI](https://www.NewsAPI.org)

## 📁 Project Structure
<pre>
newsapi-keyword-ranker/
├── README.md
├── METHODOLOGY.md
├── HOW_TO_USE.md
├── .gitignore
├── src/
│   └── fetch_news.py
│   └── db_utils.py
│   └── keyword_extractor.py
│   └── daily_keyword_pipeline.py
│   └── visualise_keywords.py
├── sql/
│   └── create_tables.sql
│   └── drop_tables.sql
├── charts/
│   └── top_keywords_2025-07-02.png
└── data/
    └── sample_response.json
</pre>

## 🛠️ How to Use

📘 See full setup instructions in [HOW_TO_USE.md](HOW_TO_USE.md)


## 🚀 Future Ideas

- Sentiment analysis of headlines
- Topic-based keyword tracking
- Dashboard or web front-end

## 📌 Data Source and Usage Disclaimer

This project uses [NewsAPI.org](https://newsapi.org/) to collect and analyze news metadata.

⚠️ All data retrieved from NewsAPI is subject to their [Terms of Use](https://newsapi.org/terms).

This repository does **not** include or redistribute any raw article content or data due to licensing restrictions.