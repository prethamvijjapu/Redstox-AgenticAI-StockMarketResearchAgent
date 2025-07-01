import yfinance as yf
import pandas as pd
import numpy as np

def get_stock_data(symbol):
    return yf.download(symbol, period="6mo", interval="1d")

def add_technical_indicators(df):
    df["SMA_50"] = df["Close"].rolling(50).mean()
    df["SMA_200"] = df["Close"].rolling(200).mean()
    df["RSI"] = compute_rsi(df["Close"])
    return df

def compute_rsi(series, period=14):
    delta = series.diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(period).mean()
    avg_loss = loss.rolling(period).mean()
    rs = avg_gain / avg_loss
    return 100 - (100 / (1 + rs))
