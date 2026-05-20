import os

from sqlalchemy import create_engine
from sqlalchemy import text

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

DATABASE_URL = (
    f"postgresql+pg8000://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS news_sentiment (

    id SERIAL PRIMARY KEY,

    title TEXT,
    source TEXT,
    published_at TEXT,
    url TEXT,

    sentiment VARCHAR(50),
    sentiment_score FLOAT
);
"""


def save_to_rds(processed_articles):

    with engine.connect() as connection:

        connection.execute(text(CREATE_TABLE_QUERY))

        insert_query = text("""

            INSERT INTO news_sentiment (
                title,
                source,
                published_at,
                url,
                sentiment,
                sentiment_score
            )

            VALUES (
                :title,
                :source,
                :published_at,
                :url,
                :sentiment,
                :sentiment_score
            )

        """)

        for article in processed_articles:

            connection.execute(
                insert_query,
                article
            )

        connection.commit()

    print("Saved into RDS successfully")