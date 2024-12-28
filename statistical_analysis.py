from scipy.stats import ttest_1samp

def hypothesis_test(data):
    recent_returns = data['Daily_Return'].iloc[-30:]
    historical_mean = data['Daily_Return'].mean()

    t_stat, p_value = ttest_1samp(recent_returns, historical_mean)
    return t_stat, p_value

if __name__ == "__main__":
    from data_loader import load_data, preprocess_data
    
    file_path = 'Amazon_Stock_Data.csv'
    data = preprocess_data(load_data(file_path))

    t_stat, p_value = hypothesis_test(data)
    print(f"T STATISTIC: {t_stat}, P-value: {p_value}")
    