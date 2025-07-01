import os
from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
DATABRICKS_TOKEN = os.getenv("DATABRICKS_TOKEN")

BASE_URL = "https://adb-3846979831828051.11.azuredatabricks.net/serving-endpoints"
KEYWORDS = ["stock", "market", "finance", "trading"]
