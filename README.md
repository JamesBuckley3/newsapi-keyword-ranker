# 📰 NewsAPI Keyword Pipeline

Automatically fetches daily top-headline news articles, extracts keywords from the titles, ranks them by frequency, and stores the results in a PostgreSQL database. Each day, it generates a bar chart of the top keywords and saves it locally. Additional NLP tagging analysis is supported.

## 🔧 Features

- Fetches global news headlines from NewsAPI
- Cleans and deduplicates data
- Stores articles, sources, and keyword rankings in PostgreSQL
- Generates a daily bar chart of trending keywords
- Analysis using SQL queries and NLP tagging

## 📦 Technologies

![Python](images/python_logo.png "Python")&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![PostgreSQL](images/postgresql_logo.png "PostgreSQL")&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![DBeaver](images/dbeaver_logo.png "DBeaver")&nbsp;&nbsp;&nbsp;&nbsp;![VSCode](images/vscode_logo.png "VSCode")

- Python (requests, psycopg2, matplotlib, NLTK, spaCy)
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
│   └── run_pipeline.bat
│   └── nlp_tagging_keywords.py
├── sql/
│   └── create_tables.sql
│   └── drop_tables.sql
|   └── *.sql  ← (additional analysis queries)
├── charts/
│   └── top_keywords_2025-07-08.png ← (example chart output)
└── data/
    └── sample_response.json
    └── keyword_rankings_20250708.csv ← (example exported keyword data)
    └── keyword_nlp_analysis.csv ← (example NLP tagging of above data)
</pre>

## 🛠️ How to Use

📘 See full setup instructions in [HOW_TO_USE.md](HOW_TO_USE.md)

## 🔍 Featured SQL Queries

| Query | Description |
|-------|-------------|
| [top_kw_daily.sql](./sql/top_kw_daily.sql) | Extracts the #1 keyword for each day. |
| [rank_change.sql](./sql/rank_change.sql) | Shows the change in a keyword's rank from yesterday. |
| [earliest_mention.sql](./sql/earliest_mention.sql) | Identifies when a chosen keyword first appeared in the dataset. |

## 🧠 NLP Tagging

This project includes a script to apply Natural Language Processing (NLP) on your keyword rankings using spaCy.


The script performs tagging on **unique keywords**:
- **Part-of-Speech (POS)** — Labels words as nouns, verbs, adjectives, etc.
- **Named Entity Recognition (NER)** — Detects known entities like people, organizations, and dates.

## 📌 Data Source and Usage Disclaimer

This project uses [NewsAPI.org](https://newsapi.org/) to collect and analyze news metadata.

⚠️ All data retrieved from NewsAPI is subject to their [Terms of Use](https://newsapi.org/terms).

This repository does **not** include or redistribute any raw article content or data due to licensing restrictions.