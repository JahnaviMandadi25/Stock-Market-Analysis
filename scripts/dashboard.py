import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data_file = "data/AAPL_prepared.csv"
stock_data = pd.read_csv(data_file, parse_dates=["Date"], index_col="Date")

# Streamlit app
st.title("Apple Stock Analysis Dashboard")

# Overview of data
st.header("Stock Data")
st.write(stock_data.tail())

# Plot Stock Prices and Moving Averages
st.header("Stock Prices and Moving Averages")
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(stock_data["Close"], label="Close Price", color="blue")
ax.plot(stock_data["50_MA"], label="50-Day Moving Average", color="green")
ax.plot(stock_data["200_MA"], label="200-Day Moving Average", color="red")
ax.set_title("Apple Stock Prices with Moving Averages")
ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.legend()
st.pyplot(fig)

# Daily Returns
st.header("Daily Returns")
st.line_chart(stock_data["Daily_Returns"])

# Volatility
st.header("30-Day Rolling Volatility")
st.line_chart(stock_data["Volatility"])
