import yfinance as yf
import pandas as pd

# Define the stock symbol and date range
stock_symbol = "AAPL"  # Apple Inc.
start_date = "2023-01-01"
end_date = "2024-01-01"

# Fetch stock data
print(f"Fetching data for {stock_symbol}...")
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Save the data to a CSV file in the 'data' folder
output_file = f"data/{stock_symbol}_data.csv"
stock_data.to_csv(output_file)

print(f"Data saved to {output_file}")
