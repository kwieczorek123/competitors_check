import yfinance as yf
import pandas as pd
import warnings
from index_constituents import *

# Suppress future warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Define your index constituents with tickers and weights
# This should be replaced with the actual way you obtain your constituents
index_constituents = {
    '^GSPC': {'tickers_weights': sp500_constituents, 'spread': 1.5},
    '^NDX': {'tickers_weights': nas100_constituents, 'spread': 3.3},
    '^DJI': {'tickers_weights': us30_constituents, 'spread': 6.6},
}


def process_index_dividends(index_name, tickers_weights, spread):
    # Initialize DataFrames at the start of the function
    all_dividends_df = pd.DataFrame(columns=["Ticker", "Ex-Date", "Dividend",
                                             "Closing Price On Ex-Date", "Dividend Yield",
                                             "Weighted Yield"])

    daily_weighted_yields_df = pd.DataFrame(columns=['Date', 'Sum Weighted Yields',
                                                     'Index Price', 'Spread/Price Ratio',
                                                     'Yield/Spread Ratio'])

    for ticker, weight in tickers_weights.items():
        stock = yf.Ticker(ticker)
        try:
            dividends = stock.dividends
            if isinstance(dividends.index, pd.DatetimeIndex):
                dividends_2023 = dividends[dividends.index.year == 2023]
                for ex_date, dividend in dividends_2023.items():
                    history = stock.history(period="1d", start=ex_date)
                    if not history.empty:
                        closing_price = history.iloc[0]['Close']
                        dividend_yield = dividend / closing_price
                        weighted_yield = dividend_yield * weight

                        # Append new row to the DataFrame
                        new_row = {"Ticker": ticker, "Ex-Date": ex_date, "Dividend": dividend,
                                   "Closing Price On Ex-Date": closing_price,
                                   "Dividend Yield": dividend_yield, "Weighted Yield": weighted_yield}
                        all_dividends_df = all_dividends_df._append(new_row, ignore_index=True)
        except Exception as e:
            print(f"An error occurred for {ticker}: {e}")

    # Ensure 'Ex-Date' is datetime format for sorting and grouping
    all_dividends_df['Ex-Date'] = pd.to_datetime(all_dividends_df['Ex-Date'])
    all_dividends_df.sort_values(by='Ex-Date', inplace=True)

    # Calculations and saving to CSV happens after the loop
    for date, grouped_data in all_dividends_df.groupby('Ex-Date'):
        sum_weighted_yields = grouped_data['Weighted Yield'].sum()
        # Ensure you handle days where the index might not have traded
        try:
            index_price = yf.Ticker(index_name).history(period="1d", start=date)['Close'].iloc[0]
            spread_over_price = spread / index_price
            ratio = sum_weighted_yields / spread_over_price
            daily_weighted_yields_df = daily_weighted_yields_df._append({
                'Date': date,
                'Sum Weighted Yields': sum_weighted_yields,
                'Index Price': index_price,
                'Spread/Price Ratio': spread_over_price,
                'Yield/Spread Ratio': ratio
            }, ignore_index=True)
        except IndexError:
            print(f"No trading data for index {index_name} on {date}")

    # Saving DataFrames to CSV
    all_dividends_df.to_csv(f"{index_name}_dividends_weighted_yields_2023.csv", index=False)
    daily_weighted_yields_df.to_csv(f"{index_name}_daily_weighted_yields_2023.csv", index=False)


# Replace this with the actual way to obtain your constituents and spread
sp500_constituents = index_constituents['^GSPC']['tickers_weights']
nas100_constituents = index_constituents['^NDX']['tickers_weights']
us30_constituents = index_constituents['^DJI']['tickers_weights']
sp500_spread = index_constituents['^GSPC']['spread']
nas100_spread = index_constituents['^NDX']['spread']
us30_spread = index_constituents['^DJI']['spread']

# Process each index
for index_name, data in index_constituents.items():
    process_index_dividends(index_name, data['tickers_weights'], data['spread'])
