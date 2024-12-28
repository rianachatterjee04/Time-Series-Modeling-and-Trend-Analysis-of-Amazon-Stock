from data_loader import load_data, preprocess_data
from eda import plot_prices_with_moving_averages, plot_volatility
from statistical_analysis import hypothesis_test
from predictive_model import forecast_prices
from export_for_tableau import save_processed_data

def main():
    # Step 1: Load and preprocess the data
    file_path = 'Amazon_Stock_Data.csv'  # Update with your file path
    output_path = 'processed_amazon_stock_data.csv'  # Update with your desired output path

    print("Loading and preprocessing data...")
    data = load_data(file_path)
    data = preprocess_data(data)
    print("Data successfully loaded and preprocessed.")

    # Step 2: Perform Exploratory Data Analysis
    print("Generating exploratory visualizations...")
    plot_prices_with_moving_averages(data)
    plot_volatility(data)

    # Step 3: Conduct Statistical Analysis
    print("Performing hypothesis testing...")
    t_stat, p_value = hypothesis_test(data)
    print(f"Hypothesis Test Results:\nT-statistic: {t_stat}, P-value: {p_value}")

    # Step 4: Forecast Stock Prices
    print("Forecasting future stock prices...")
    forecast = forecast_prices(data)
    print("Forecast completed.")

    # Step 5: Export Data for Tableau
    print("Exporting processed data for Tableau...")
    save_processed_data(data, output_path)
    print(f"Data successfully exported to {output_path}")

if __name__ == "__main__":
    main()
