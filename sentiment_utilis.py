import requests
from newspaper import Article
from config import NEWS_API_KEY, KEYWORDS
from analysis_utils import analyze_with_claude

def fetch_stock_news(symbol):
    url = f"https://newsapi.org/v2/everything?q={symbol}&apiKey={NEWS_API_KEY}"
    res = requests.get(url).json()
    articles = res.get("articles", [])
    filtered = []
    for a in articles:
        if any(k in a["title"].lower() for k in KEYWORDS):
            filtered.append({"url": a["url"], "title": a["title"], "date": a["publishedAt"]})
    return filtered

def fetch_full_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception:
        return ""

def summarize_sentiment(text, prompt_template):
    sentiment = analyze_with_claude(prompt_template + "\n\nClassify sentiment:", text)
    summary = analyze_with_claude(prompt_template + "\n\nSummarize in 3 points:", text)
    return sentiment, summary
