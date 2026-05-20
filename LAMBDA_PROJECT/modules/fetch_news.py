import os
import requests

API_KEY = os.environ.get("NEWS_API_KEY")

NEWS_URL = (
    f"https://newsapi.org/v2/top-headlines?"
    f"country=us&apiKey={API_KEY}"
)


def fetch_news():

    response = requests.get(NEWS_URL)

    response.raise_for_status()

    return response.json()