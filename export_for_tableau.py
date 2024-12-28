def save_processed_data(data, output_path):
    data.to_csv(output_path, index=False)

if __name__ == "__main__":
    from data_loader import load_data, preprocess_data

    file_path = 'Amazon_Stock_Data.csv'
    output_path = 'processed_amazon_stock_data.csv'

    data = preprocess_data(load_data(file_path))
    save_processed_data(data, output_path)

    print(f"Data saved to {output_path}")