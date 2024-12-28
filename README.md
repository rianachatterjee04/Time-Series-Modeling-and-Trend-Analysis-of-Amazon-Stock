# **Time-Series Modeling and Trend Analysis of Amazon Stock** 📈

This project performs a comprehensive time-series analysis and forecasting of Amazon stock data. The pipeline includes data preprocessing, exploratory data analysis (EDA), statistical analysis, predictive modeling, and visualization.

---

## **Project Structure** 🗂️
```
Time-Series-Modeling-and-Trend-Analysis-of-Amazon-Stock/
│
├── data_loader.py              # Data loading and preprocessing script
├── eda.py                      # Exploratory Data Analysis
├── statistics_analysis.py      # Hypothesis testing and statistical analysis
├── predictive_model.py         # Forecasting with Facebook Prophet
├── export_for_tableau.py       # Export data for Tableau visualization
├── main.py                     # Pipeline orchestrator
├── requirements.txt            # List of dependencies
├── processed_amazon_stock_data.csv  # Processed data (output)
├── tableau_dashboard.twbx      # Tableau workbook (optional)
└── README.md                   # Project documentation
```

---

## **Table of Contents** 📋
1. [Introduction](#introduction)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Data Pipeline](#data-pipeline)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Visualizations and Insights](#visualizations-and-insights)
8. [Future Work](#future-work)
9. [Acknowledgments](#acknowledgments)

---

## **Introduction** 🌟
The project leverages Amazon stock data to explore historical trends, conduct statistical analyses, and forecast future prices. The end goal is to provide actionable insights through interactive Tableau dashboards and visualizations.

---

## **Features** ✨
- **Data Preprocessing**:
  - Calculates rolling averages, daily returns, and volatility.
- **Exploratory Data Analysis**:
  - Visualizes stock trends and volatility.
- **Statistical Analysis**:
  - Performs hypothesis testing on stock returns.
- **Predictive Modeling**:
  - Uses Facebook Prophet to forecast future stock prices.
- **Export for Tableau**:
  - Outputs processed data for creating interactive dashboards.

---

## **Technologies Used** 💻
- **Programming**:
  - Python
- **Libraries**:
  - Pandas, Matplotlib, Scipy, Prophet
- **Visualization**:
  - Tableau
- **Version Control**:
  - Git and GitHub

---

## **Data Pipeline** 🔄
1. **Data Loading**:
   - Load raw Amazon stock data from a CSV file.
2. **Preprocessing**:
   - Add rolling averages (`30_day_MA`, `90_day_MA`), daily returns, and volatility.
3. **Exploratory Analysis**:
   - Visualize trends and distributions.
4. **Statistical Analysis**:
   - Hypothesis testing to evaluate recent stock behavior.
5. **Predictive Modeling**:
   - Use Prophet to generate stock price forecasts.
6. **Export for Tableau**:
   - Save the processed dataset for use in Tableau dashboards.

---

## **Installation** 🛠️
1. Clone the repository:
   ```bash
   git clone https://github.com/rianachatterjee04/Time-Series-Modeling-and-Trend-Analysis-of-Amazon-Stock.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Time-Series-Modeling-and-Trend-Analysis-of-Amazon-Stock
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage** 🚀
1. **Run the main script** to process the data and generate outputs:
   ```bash
   python3 main.py
   ```
2. **Access Tableau Dashboards**:
   - Open the processed dataset (`processed_amazon_stock_data.csv`) in Tableau.
   - Use the provided Tableau workbook or create your own visualizations.

---

## **Visualizations and Insights** 📊
The following visualizations are included in the Tableau dashboard:
1. **Stock Price Trends**:
   - Line chart with `Close`, `30_day_MA`, and `90_day_MA`.
2. **Daily Returns Histogram**:
   - Distribution of daily return percentages.
3. **Volatility Trend**:
   - Fluctuations in rolling volatility over time.
4. **Forecasted Stock Prices**:
   - Predicted future prices with confidence intervals.
5. **Statistical Insights**:
   - T-statistic and p-value from hypothesis testing.

---

## **Future Work** 🔮
- Include additional financial metrics (e.g., moving average convergence divergence, RSI).
- Enhance model predictions with external factors like market indices or news sentiment.
- Automate Tableau dashboard updates with live data feeds.

---

## **Acknowledgments** 🙏
- **Data Source**: [Kaggle - Amazon Stock Data](https://www.kaggle.com/).
- Special thanks to the open-source tools and libraries that made this project possible.

---
