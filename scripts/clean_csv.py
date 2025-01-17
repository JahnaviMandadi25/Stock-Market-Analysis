import pandas as pd

# Load the raw file without assuming headers
input_file = "data/AAPL_data.csv"
output_file = "data/AAPL_cleaned.csv"

# Skip unnecessary rows and extract the actual table
with open(input_file, "r") as f:
    lines = f.readlines()

# Identify the row where the actual data starts (e.g., after "Date")
for i, line in enumerate(lines):
    if line.startswith("Date"):  # Adjust this condition if needed
        data_start = i
        break

# Load the data from the identified row
stock_data = pd.read_csv(input_file, skiprows=data_start)

# Print the current column names and count
print("Column names before renaming:", stock_data.columns)
print("Number of columns:", len(stock_data.columns))

# Uncomment the next line to inspect the data visually
# print(stock_data.head())

# Rename the columns explicitly based on the actual structure
stock_data.columns = ["Date", "Open", "High", "Low", "Close", "Volume"]  # Adjust to match the number of columns

# Save the cleaned file
stock_data.to_csv(output_file, index=False)
print(f"Cleaned data saved to {output_file}")
