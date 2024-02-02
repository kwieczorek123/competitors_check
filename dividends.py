import yfinance as yf
import pandas as pd
import warnings
from index_constituents import *

# Suppress future warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Define your index constituents with tickers and weights
# This should be replaced with the actual way you obtain your constituents
index_constituents = {
    'sp500': {'tickers_weights': sp500_constituents, 'spread': 0.3},
    'nas100': {'tickers_weights': nas100_constituents, 'spread': 0.35},
    'us30': {'tickers_weights': us30_constituents, 'spread': 0.8},
}


def process_index_dividends(index_name, tickers_weights, spread):
    # Initialize an empty DataFrame to store all dividend data
    all_dividends_df = pd.DataFrame()

    # Initialize an empty DataFrame to store daily weighted yields
    daily_weighted_yields_df = pd.DataFrame()

    for ticker, weight in tickers_weights.items():
    # ... Your logic to fetch and calculate dividends and yields as before

    # Now, calculate the additional metrics for each date
    for date, grouped_data in all_dividends_df.groupby('Ex-Date'):
        sum_weighted_yields = grouped_data['Weighted Yield'].sum()
        index_price = yf.Ticker(index_name).history(period="1d", start=date)['Close'][0]
        spread_over_price = spread / index_price
        ratio = sum_weighted_yields / spread_over_price
        daily_weighted_yields_df = daily_weighted_yields_df.append({
            'Date': date,
            'Sum Weighted Yields': sum_weighted_yields,
            'Index Price': index_price,
            'Spread/Price Ratio': spread_over_price,
            'Yield/Spread Ratio': ratio
        }, ignore_index=True)

    # Save the individual index dividends data to a CSV file
    all_dividends_df.to_csv(f"{index_name}_dividends_weighted_yields_2023.csv", index=False)

    # Save the daily weighted yields data to a CSV file
    daily_weighted_yields_df.to_csv(f"{index_name}_daily_weighted_yields_2023.csv", index=False)


# Replace this with the actual way to obtain your constituents and spread
sp500_constituents = {...}
nas100_constituents = {...}
us30_constituents = {...}
sp500_spread = ...
nas100_spread = ...
us30_spread = ...

# Process each index
for index_name, data in index_constituents.items():
    process_index_dividends(index_name, data['tickers_weights'], data['spread'])
