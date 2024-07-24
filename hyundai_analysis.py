import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from graphviz import Digraph

def define_problem():
    print("Step 1: Define the Problem or Research Question")
    print("Research Question: How has Hyundai Motor Company's financial performance, market share, and vehicle sales evolved over recent years?")
    print("Objective: To analyze the financial health, stock performance, market share, and vehicle sales trends of Hyundai Motor Company.")

def collect_data():
    print("\nStep 2: Collect Data")
    print("Collecting financial data, stock data, market share data, and vehicle sales data...")
    ticker = '005380.KS'  # Hyundai Motor Company's ticker symbol on the Korea Exchange
    financials, balance_sheet, cash_flow = get_financial_data(ticker)
    stock_data = get_stock_data(ticker)
    print("Data collection completed.")
    return financials, balance_sheet, cash_flow, stock_data

def data_cleaning(financials, balance_sheet, cash_flow, stock_data):
    print("\nStep 3: Data Cleaning")
    print("Cleaning and formatting the collected data...")
    # Here you would implement any necessary data cleaning steps
    print("Data cleaning completed.")

def analyzing_data(financials, balance_sheet, cash_flow, stock_data):
    print("\nStep 4: Analyzing the Data")
    print("Performing analysis on financial data, stock data, market share data, and vehicle sales data...")
    # Here you would perform your data analysis
    print("Data analysis completed.")
    return financials, balance_sheet, cash_flow, stock_data

def data_visualization(financials, balance_sheet, cash_flow, stock_data):
    print("\nStep 5: Data Visualization")
    print("Creating visualizations for the analyzed data...")
    plot_financial_data(financials)
    plot_balance_sheet(balance_sheet)
    plot_cash_flow(cash_flow)
    plot_stock_data(stock_data)
    plot_revenue_profit(financials)
    plot_market_share(market_share)
    plot_vehicle_sales(vehicle_sales)
    print("Data visualization completed.")

def presenting_data():
    print("\nStep 6: Presenting Data")
    print("Presenting the findings through visual representations and a summary of key insights.")
    visualize_data_pipeline()
    print("Data presentation completed.")

# Functions to fetch and process data
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

# Plotting functions
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

# Function to visualize data collection and processing pipeline
def visualize_data_pipeline():
    dot = Digraph()

    # Add nodes for each step in the process
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

    # Add edges to represent the flow of data
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

    # Save and render the graph
    dot.render('data_pipeline', format='pdf', view=True)

# Main function
if __name__ == "__main__":
    define_problem()
    financials, balance_sheet, cash_flow, stock_data = collect_data()
    data_cleaning(financials, balance_sheet, cash_flow, stock_data)
    financials, balance_sheet, cash_flow, stock_data = analyzing_data(financials, balance_sheet, cash_flow, stock_data)
    data_visualization(financials, balance_sheet, cash_flow, stock_data)
    presenting_data()
