import streamlit as st
from technical_utils import get_stock_data, add_technical_indicators
from sentiment_utils import fetch_stock_news, fetch_full_article, summarize_sentiment
from agents import RESEARCHER_AGENTS
from analysis_utils import analyze_with_claude

def home_page():
    st.title("📊 Redstox: Stock Analysis Dashboard")
    symbol = st.text_input("Enter stock symbol (e.g., AAPL)")
    if not symbol:
        return

    st.subheader("1. Technical Analysis")
    df = get_stock_data(symbol)
    df = add_technical_indicators(df)
    st.line_chart(df[["Close", "SMA_50", "SMA_200"]].dropna())

    st.subheader("2. Sentiment Analysis")
    news = fetch_stock_news(symbol)
    for item in news[:2]:
        st.markdown(f"**{item['title']}**")
        full_text = fetch_full_article(item["url"])
        sentiment, summary = summarize_sentiment(full_text, "As a financial analyst")
        st.write(f"Sentiment: {sentiment}")
        st.markdown(summary)

    st.subheader("3. Fundamental (AI) Analysis")
    persona = st.selectbox("Choose Analyst Persona", list(RESEARCHER_AGENTS.keys()))
    template = RESEARCHER_AGENTS[persona]["template"]
    st.markdown("Upload stock data (from Yahoo Finance) for AI analysis:")
    uploaded_file = st.file_uploader("Upload .txt or .csv file")
    if uploaded_file:
        content = uploaded_file.read().decode("utf-8")
        result = analyze_with_claude(template, content)
        st.markdown(result)

def setup_ui():
    PAGES = {
        "Home": home_page,
        # You can add more pages here
    }

    st.sidebar.title("Redstox Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page()
