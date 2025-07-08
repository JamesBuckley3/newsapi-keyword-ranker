# 🛠️ How to Use the NewsAPI Keyword Ranking Pipeline

This guide walks you through setting up and running the pipeline that fetches daily news, extracts top keywords from article titles, and visualizes them in a bar chart — all powered by NewsAPI and PostgreSQL.

---

## 📦 Requirements

- Python 3.8+ and required packages (`matplotlib`, `requests`, `nltk` and `psycopg2`)
    - Optional: `spaCy` for NLP tagging
- PostgreSQL (e.g. via pgAdmin or CLI)
- A [NewsAPI](https://newsapi.org) API key

---

## ✅ 1. Create the Database Tables

1. Open pgAdmin (or your PostgreSQL tool of choice)
2. Create a database, e.g. `newsapi_pipeline`
3. Execute the SQL setup script:

```sql
-- In pgAdmin query tool or terminal with psql:
-- Connect to your database first, then run:
sql/create_tables.sql
```

---

## 🔐 2. Add Your NewsAPI Key

Edit src/fetch_news.py:

```python
API_KEY = "your_api_key_here"
```
Get your key from https://newsapi.org/account.

---

## 🌍 3. Choose Your News Topics

In the same fetch_news.py file, change the TOPICS list to track the topics of your choice (max 100). Default:

```python
TOPICS = ["technology", "climate", "economy", "politics", "health", "sports"]
```

These will be used to search news from the previous day.

---

## ⚙️ 4. Configure Database Access

Edit src/db_utils.py and update your credentials:

```python
DB_PARAMS = {
    "dbname": "newsapi_pipeline",
    "user": "your_username",
    "password": "your_password",
    "host": "localhost",
    "port": 5432,
}
```

---

## 🦇 5. Edit run_pipeline.bat

Update the following line with the path to your Python environment.
```batch
"C:\YourPythonEnvironmentFolder\python.exe" "src\daily_keyword_pipeline.py"
```
---

## ⏰ 6. Automate Daily Pipeline Runs (Windows)

You can schedule the pipeline to run daily using Windows Task Scheduler, ensuring your data and charts stay up to date without manual work.

### ✅ Before You Begin

Make sure:

- Your Python environment is installed and working

- Required packages are installed on same Python environment:
    - psycopg2
    - requests
    - nltk
    - matplotlib


### 🧭 Set Up a Daily Task

1. Open Task Scheduler

    - Press Win + R, type taskschd.msc, hit Enter

     - Or search “Task Scheduler” in the Start menu

2. Create a Basic Task

    - Click "Create Basic Task…"

    - Name: Daily News Keyword Pipeline (or whatever you'd like)

    - Choose trigger: Daily

    - Set the time (e.g., 09:00 AM)

    - Choose action: "Start a program"

3. Select Your Batch File

    - Program/script: Full path to your run_pipeline.bat file
    
        Example:
        ```makefile
        C:\Users\YourName\Documents\newsapi-keyword-ranker\src\run_pipeline.bat
        ```
    - Start in (optional): The folder where the .bat file is located

4. Open Advanced Settings

    - ✅ Check "Open the Properties dialog…" before finishing

    - In the General tab:

        - Select "Run whether user is logged on or not"

        - Provide your Windows account password if prompted

    - In the Settings tab:

        - Set: "Stop the existing instance" if the task is already running

        - Optional: Limit task duration (e.g., stop if it runs over 1 hour)

### 🔍 Test & Verify

- Right-click your task → Run

- Confirm the chart .png appears in the charts/ folder

- A successful run shows Last Run Result: (0x0)

- If it fails, check:

    - Python path in your .bat file

    - Windows Task Scheduler history

    - Output console from the script (keep pause in the .bat for debugging)

---

## 🖐️ 6. Run Manually (Optional)

To run the pipeline manually:

1. Open your src/ folder

2. Double-click run_pipeline.bat

3. Watch the command prompt for any output or errors (thanks to pause)

4. Check your charts/ folder for the new image

---

## 📜 Analyse with SQL scripts

In your database tool of choice you can gain insights on the data tables by executing the SQL queries in the `sql` folder. 

Most of the scripts are focused on keyword analysis (rankings, trends, etc).

---

## 📊 Analyse with NLP

Once you've exported your `keyword_rankings` table to a CSV file (e.g., using your database tool), you can perform NLP tagging using the included Python script.

### Steps:

1. **Export your data**  
   Export the `keyword_rankings` table as a CSV file (e.g., `keyword_rankings.csv`).

2. **Update file paths**  
   Open `src/nlp_tagging_keywords.py` and update the `read_csv()` and `to_csv()` file paths to match your file locations.

3. **Run the script**  
   Execute the script using Python:

   ```bash
   python src/nlp_tagging_keywords.py
   ```

### What it does:

The script performs two types of NLP tagging on each unique keyword:

- **Part-of-Speech (POS)** – Labels each word as a noun, verb, adjective, etc.

- **Named Entity Recognition (NER)** – Identifies entities like people, organizations, locations, and dates.

### Output:

You’ll get a new CSV file (e.g., keyword_nlp_analysis.csv) containing enriched information for each keyword, including:

- `pos` (e.g., NOUN, VERB)

- `tag` (fine-grained POS)

- `lemma` (base word form)

- `entity` (NER label, if applicable)

- `is_entity` (True/False)

- `extracted_entity_text` (e.g., “Bezos” → PERSON)