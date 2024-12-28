import matplotlib.pyplot as plt

def plot_prices_with_moving_averages(data):
    plt.figure(figsize = (12,6))
    plt.plot(data['Date'], data['Close'], label='Close Price')
    plt.plot(data['Date'], data ['30_day_MA'], label= '30-Day-MA', linestyle='--')
    plt.plot(data['Date'], data ['90_day_MA'], label= '90-Day-MA', linestyle='--')
    plt.title('Amazon Stock Prices with Moving Averages')
    plt.legend()
    plt.show()

def plot_volatility(data):
    plt.figure(figsize = (12,6))
    plt.plot(data['Date'], data['Volatility'], label = '30-Day Volatility')
    plt.title('Volatility of Daily Returns')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    from data_loader import load_data, preprocess_data

    file_path = 'Amazon_Stock_Data.csv'
    data = preprocess_data(load_data(file_path))

    plot_prices_with_moving_averages(data)
    plot_volatility(data)