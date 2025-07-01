📈 Redstox: AI-Powered Stock Analysis Platform

Redstox is an LLM-powered investment research agent that delivers real-time stock insights through fundamental, technical, and sentiment analysis — all accessible via a clean Streamlit interface.

---

## 🚀 Features

- 💼 Fundamental Analysis
  Uses Claude 3 Sonnet to simulate investing strategies from legends like Buffett, Lynch, and Dalio.

- 📊 Technical Analysis
  Calculates indicators such as SMA, RSI, and Bollinger Bands, and displays interactive charts with Plotly.

- 📰 Sentiment Analysis
  Scrapes real-time news using NewsAPI and Newspaper3k, then classifies sentiment using FinBERT and Claude.

- 🧠 AI Query Engine
  Users can ask stock-related questions and receive expert-style responses powered by prompt-engineered Claude LLMs.

---

## 🧱 Tech Stack

| Layer       | Tools / Technologies                                   |
|-------------|--------------------------------------------------------|
| UI          | Streamlit                                              |
| Data APIs   | Yahoo Finance (via `yfinance`), NewsAPI, Newspaper3k   |
| LLM Engine  | Claude 3.7 Sonnet via Azure Databricks                 |
| Vector DB   | Pinecone (for document embeddings - future use)        |
| Backend     | Python, LangChain (partial), OpenAI SDK                |
| Visualization | Plotly                                               |

