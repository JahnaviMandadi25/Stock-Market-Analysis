import pandas as pd

# Load the cleaned stock data
input_file = "data/AAPL_cleaned.csv"
stock_data = pd.read_csv(input_file, parse_dates=["Date"], index_col="Date")

# Check for missing values
print("Checking for missing values...")
print(stock_data.isnull().sum())

# Add new columns
# Daily Returns
stock_data["Daily_Returns"] = stock_data["Close"].pct_change()

# Moving Averages (50-day and 200-day)
stock_data["50_MA"] = stock_data["Close"].rolling(window=50).mean()
stock_data["200_MA"] = stock_data["Close"].rolling(window=200).mean()

# Volatility (30-day rolling standard deviation of returns)
stock_data["Volatility"] = stock_data["Daily_Returns"].rolling(window=30).std()

# Save the processed data to a new CSV
output_file = "data/AAPL_prepared.csv"
stock_data.to_csv(output_file)

print(f"Prepared data saved to {output_file}")
