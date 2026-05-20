import os
from dotenv import load_dotenv

load_dotenv()

# ==============================
# NEWS API
# ==============================

API_KEY = os.getenv("API_KEY")

URL = (
    f"https://newsapi.org/v2/top-headlines?"
    f"country=us&"
    f"category=business&"
    f"apiKey={API_KEY}"
)

# ==============================
# DATABASE CONFIG
# ==============================

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = (
    f"postgresql+pg8000://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ==============================
# AWS S3
# ==============================

S3_BUCKET = os.getenv("S3_BUCKET")
AWS_REGION = os.getenv("AWS_REGION")