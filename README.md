
# Hyundai Motor Company Data Analysis

This repository contains a comprehensive analysis of Hyundai Motor Company's financial performance, market share, and vehicle sales. The analysis includes data collection, cleaning, analysis, visualization, and presentation of key insights.

## Table of Contents
- [Problem Definition](#problem-definition)
- [Data Collection](#data-collection)
- [Data Cleaning](#data-cleaning)
- [Data Analysis](#data-analysis)
- [Data Visualization](#data-visualization)
- [Data Presentation](#data-presentation)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [References](#references)

## Problem Definition
### Research Question
How has Hyundai Motor Company's financial performance, market share, and vehicle sales evolved over recent years?

### Objective
To analyze the financial health, stock performance, market share, and vehicle sales trends of Hyundai Motor Company.

## Data Collection
We collect the following types of data:
1. **Financial Data**: Income statements, balance sheets, and cash flow statements from Yahoo Finance.
2. **Stock Data**: Historical stock prices and trading volumes from Yahoo Finance.
3. **Market Share Data**: Data sourced from market research reports.
4. **Vehicle Sales Data**: Sales data from industry reports.

### Code for Data Collection
```python
import yfinance as yf
import pandas as pd

def get_financial_data(ticker):
    stock = yf.Ticker(ticker)
    financials = stock.financials.T
    balance_sheet = stock.balance_sheet.T
    cash_flow = stock.cashflow.T
    return financials, balance_sheet, cash_flow

def get_stock_data(ticker, period='5y'):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    return hist

ticker = '005380.KS'
financials, balance_sheet, cash_flow = get_financial_data(ticker)
stock_data = get_stock_data(ticker)

# Example market share and vehicle sales data
market_share_data = {'Region': ['North America', 'Europe', 'Asia'], 'Market Share': [10, 15, 20]}
market_share = pd.DataFrame(market_share_data)

vehicle_sales_data = {'Vehicle Type': ['Sedan', 'SUV', 'Truck'], 'Sales': [50000, 30000, 20000]}
vehicle_sales = pd.DataFrame(vehicle_sales_data)
```

## Data Cleaning
Cleaning and formatting the collected data to ensure it is ready for analysis.

```python
def data_cleaning(financials, balance_sheet, cash_flow, stock_data):
    # Implement necessary data cleaning steps
    print("Data cleaning completed.")
```

## Data Analysis
Performing analysis on financial data, stock data, market share data, and vehicle sales data.

```python
def analyzing_data(financials, balance_sheet, cash_flow, stock_data):
    # Implement data analysis
    print("Data analysis completed.")
    return financials, balance_sheet, cash_flow, stock_data
```

## Data Visualization
Creating visualizations for the analyzed data.

```python
import matplotlib.pyplot as plt
import seaborn as sns

def plot_financial_data(financials):
    plt.figure(figsize=(12, 6))
    financials.plot(kind='bar')
    plt.title('Financial Data (in millions)')
    plt.ylabel('Amount')
    plt.xlabel('Year')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

def plot_stock_data(stock_data):
    plt.figure(figsize=(12, 6))
    plt.plot(stock_data['Close'], label='Close Price')
    plt.title('Stock Price History')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

def plot_balance_sheet(balance_sheet):
    plt.figure(figsize=(12, 6))
    balance_sheet.plot(kind='bar')
    plt.title('Balance Sheet Data (in millions)')
    plt.ylabel('Amount')
    plt.xlabel('Year')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

def plot_cash_flow(cash_flow):
    plt.figure(figsize=(12, 6))
    cash_flow.plot(kind='bar')
    plt.title('Cash Flow Data (in millions)')
    plt.ylabel('Amount')
    plt.xlabel('Year')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

def plot_revenue_profit(financials):
    plt.figure(figsize=(12, 6))
    financials[['Total Revenue', 'Gross Profit']].plot(kind='line')
    plt.title('Revenue and Profit (in millions)')
    plt.ylabel('Amount')
    plt.xlabel('Year')
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

def plot_market_share(market_share):
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Region', y='Market Share', data=market_share)
    plt.title('Market Share by Region')
    plt.ylabel('Market Share (%)')
    plt.xlabel('Region')
    plt.grid(True)
    plt.show()

def plot_vehicle_sales(vehicle_sales):
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Vehicle Type', y='Sales', data=vehicle_sales)
    plt.title('Vehicle Sales by Type')
    plt.ylabel('Sales (units)')
    plt.xlabel('Vehicle Type')
    plt.grid(True)
    plt.show()
```

## Data Presentation
Presenting the findings through visual representations and a summary of key insights.

```python
from graphviz import Digraph

def visualize_data_pipeline():
    dot = Digraph()

    dot.node('A', 'Data Collection')
    dot.node('B', 'Financial Data\n(yfinance API)')
    dot.node('C', 'Stock Data\n(yfinance API)')
    dot.node('D', 'Market Share Data\n(Reports/APIs)')
    dot.node('E', 'Vehicle Sales Data\n(Reports/APIs)')
    dot.node('F', 'Data Processing')
    dot.node('G', 'Data Cleaning & Formatting')
    dot.node('H', 'Metric Calculation')
    dot.node('I', 'Data Aggregation')
    dot.node('J', 'Data Visualization')
    dot.node('K', 'Financial Data Visualization')
    dot.node('L', 'Stock Data Visualization')
    dot.node('M', 'Market Share Visualization')
    dot.node('N', 'Vehicle Sales Visualization')

    dot.edge('A', 'B')
    dot.edge('A', 'C')
    dot.edge('A', 'D')
    dot.edge('A', 'E')
    dot.edge('B', 'F')
    dot.edge('C', 'F')
    dot.edge('D', 'F')
    dot.edge('E', 'F')
    dot.edge('F', 'G')
    dot.edge('F', 'H')
    dot.edge('F', 'I')
    dot.edge('G', 'J')
    dot.edge('H', 'J')
    dot.edge('I', 'J')
    dot.edge('J', 'K')
    dot.edge('J', 'L')
    dot.edge('J', 'M')
    dot.edge('J', 'N')

    dot.render('data_pipeline', format='pdf', view=True)

# Main function
if __name__ == "__main__":
    define_problem()
    financials, balance_sheet, cash_flow, stock_data = collect_data()
    data_cleaning(financials, balance_sheet, cash_flow, stock_data)
    financials, balance_sheet, cash_flow, stock_data = analyzing_data(financials, balance_sheet, cash_flow, stock_data)
    data_visualization(financials, balance_sheet, cash_flow, stock_data)
    presenting_data()
```

## Requirements
- Python 3.x
- pandas
- yfinance
- matplotlib
- seaborn
- graphviz

### Install Required Libraries
```sh
pip install pandas yfinance matplotlib seaborn graphviz
```

### Install Graphviz System Package
On some systems, you may need to install the Graphviz system package separately. For example, on Ubuntu:
```sh
sudo apt-get install graphviz
```

## How to Run
1. Clone the repository.
2. Install the required libraries.
3. Run the Python script.

```sh
python hyundai_analysis_pipeline.py
```

## References
- [Yahoo Finance](https://finance.yahoo.com/)
- [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Graphviz Documentation](https://graphviz.gitlab.io/)
