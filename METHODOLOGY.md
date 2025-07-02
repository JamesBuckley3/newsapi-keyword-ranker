# 🧠 Project Methodology: NewsAPI Data Pipeline

## 🎯 Objective
Build a Python-based ETL pipeline that ranks keywords in news stories daily from NewsAPI and stores them in a PostgreSQL database. Normalise the data into multiple relational tables (articles, sources, keywords) and use it for analysis.

---

## 📆 Timeline

### ✅ v0.1: Initial Setup
- [x] Register with NewsAPI and obtain API key
- [x] Test basic API call to fetch `everything`

### 🔄 v0.2: Daily Fetching + Storage
- [x] Design normalised schema (articles, sources, keywords)
- [x] Create tables in PostgreSQL using SQL
- [x] Write Python script to fetch and insert daily stories
- [x] Output a daily bar chart of most common keywords
- [x] Setup Windows Task Scheduling for daily automatic runs

### 📊 v0.3: Potential Analysis
- [ ] Use DBeaver to query tables
- [ ] Add NLP tagging

---

## 🧱 Schema Design

### `articles`
- `id`, `title`, `author`, `url`, `published_at`, `description`, `source_id`

### `sources`
- `id`, `name`, `url`

### `keyword_rankings`
- `id`, `keyword`, `count`, `rank`, `collected_at`

---

## 🔍 Data Sources
- [NewsAPI.org](https://newsapi.org/)

---

## 🛠 Tools Used
- Python (requests, nltk, psycopg2, matplotlib)
- PostgreSQL + pgAdmin
- VSCode