import pandas as pd
import matplotlib.pyplot as plt

# Load the prepared data
input_file = "data/AAPL_prepared.csv"
stock_data = pd.read_csv(input_file, parse_dates=["Date"], index_col="Date")

# Plot 1: Stock Prices and Moving Averages
plt.figure(figsize=(12, 6))
plt.plot(stock_data["Close"], label="Close Price", color="blue")
plt.plot(stock_data["50_MA"], label="50-Day Moving Average", color="green")
plt.plot(stock_data["200_MA"], label="200-Day Moving Average", color="red")
plt.title("Apple Stock Prices with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid()

# Save the plot to the visuals folder
plt.savefig("visuals/stock_prices_with_moving_averages.png")
plt.show()
