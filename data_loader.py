import pandas as pd

def load_data(file_path):
    """Load the stock data from a CSV file."""
    # Load the dataset and skip unnecessary rows
    data = pd.read_csv(file_path, index_col=0, skiprows=1)
    data.columns = data.columns.str.strip()  # Strip spaces from column names
    data.index.name = 'Date'  # Name the index
    data.reset_index(inplace=True)  # Move the index into a column

    # Rename columns explicitly for clarity
    data.columns = ['Date', 'Adj Close', 'Close', 'High', 'Low', 'Open', 'Volume']

    # Convert 'Date' to datetime and drop invalid rows
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data.dropna(subset=['Date'], inplace=True)

    return data


def preprocess_data(data):
    """Preprocess data by adding rolling averages, daily returns, and volatility to the dataset."""
    # Calculate rolling averages
    data['30_day_MA'] = data['Close'].rolling(window=30).mean()
    data['90_day_MA'] = data['Close'].rolling(window=90).mean()

    # Calculate daily returns
    data['Daily_Return'] = data['Close'].pct_change() * 100

    # Calculate rolling volatility
    data['Volatility'] = data['Daily_Return'].rolling(window=30).std()

    return data


if __name__ == "__main__":
    # File path to the dataset
    file_path = 'Amazon_Stock_Data.csv'  # Replace with your actual file path

    # Load the data
    print("Loading data...")
    data = load_data(file_path)
    print("Data loaded successfully!")

    # Debug: Print column names and first few rows
    print("Column names:", data.columns)
    print("First few rows:\n", data.head())

    # Preprocess the data
    print("Preprocessing data...")
    data = preprocess_data(data)
    print("Data preprocessing complete!")

    # Debug: Print first few rows of the processed data
    print("Processed data:\n", data.head())
