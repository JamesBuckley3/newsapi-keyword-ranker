CREATE TABLE IF NOT EXISTS sources (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    url TEXT
);

CREATE TABLE IF NOT EXISTS keyword_rankings (
    id SERIAL PRIMARY KEY,
    keyword TEXT,
    count INT,
    rank INT,
    collected_at DATE DEFAULT CURRENT_DATE
);

CREATE TABLE IF NOT EXISTS articles (
    id SERIAL PRIMARY KEY,
    title TEXT,
    author TEXT,
    description TEXT,
    url TEXT UNIQUE,
    published_at TIMESTAMP,
    source_id INT REFERENCES sources(id)
);
