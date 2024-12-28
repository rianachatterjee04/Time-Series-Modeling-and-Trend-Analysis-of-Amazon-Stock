from prophet import Prophet
import pandas as pd

def forecast_prices(data):
    """Use Prophet to forecast future stock prices."""
    # Prepare data for Prophet
    prophet_data = data[['Date', 'Close']].rename(columns={'Date': 'ds', 'Close': 'y'})
    model = Prophet()
    model.fit(prophet_data)

    # Forecast for the next 180 days
    future = model.make_future_dataframe(periods=180)
    forecast = model.predict(future)

    # Merge forecast with original data
    forecast = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    forecast.rename(columns={'ds': 'Date'}, inplace=True)
    return forecast

if __name__ == "__main__":
    # Load the processed data
    from data_loader import load_data, preprocess_data

    file_path = 'Amazon_Stock_Data.csv'
    output_path = 'processed_amazon_stock_data_with_forecast.csv'

    # Process and forecast data
    data = preprocess_data(load_data(file_path))
    forecast = forecast_prices(data)

    # Merge historical data with forecast
    merged_data = pd.merge(data, forecast, on='Date', how='outer')
    merged_data.to_csv(output_path, index=False)

    print(f"Forecasted data saved to {output_path}")
