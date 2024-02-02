import yfinance as yf
import pandas as pd
import warnings

# Suppress future warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Replace with your list of S&P 500 constituents
tickers_weights = {"UNH": 8.675315, "MSFT": 6.907203, "GS": 6.566273, "HD": 6.159484, "AMGN": 5.552037, "CAT": 5.263453,
                   "MCD": 5.099061, "CRM": 4.854783, "V": 4.739315, "TRV": 3.626889, "BA": 3.589084, "AXP": 3.476353,
                   "HON": 3.375254, "IBM": 3.197177, "AAPL": 3.196493, "JPM": 2.971886, "WMT": 2.87917, "PG": 2.722989,
                   "JNJ": 2.708962, "CVX": 2.529858, "MRK": 2.161901, "NKE": 1.740742, "DIS": 1.660342, "MMM": 1.64067,
                   "KO": 1.043145, "DOW": 0.915874, "CSCO": 0.858397, "INTC": 0.741731, "VZ": 0.726849, "WBA": 0.397723,
                   }

# Initialize an empty DataFrame to store dividend data with yields
dividends_yields_df = pd.DataFrame(columns=["Ticker", "Ex-Date", "Dividend", "Closing Price On Ex-Date",
                                            "Dividend Yield", "Weighted Yield"])

for ticker, weight in tickers_weights.items():
    stock = yf.Ticker(ticker)
    try:
        # Fetch dividends for the stock
        dividends = stock.dividends
        # Ensure the index is a DatetimeIndex
        if isinstance(dividends.index, pd.DatetimeIndex):
            dividends_2023 = dividends[dividends.index.year == 2023]
            for ex_date, dividend in dividends_2023.items():
                # Use the ex-date's closing price
                history = stock.history(period="1d", start=ex_date)
                if not history.empty:
                    closing_price = history.iloc[0]['Close']
                    dividend_yield = dividend / closing_price  # Calculate dividend yield
                    weighted_yield = dividend_yield * weight  # Calculate the weighted yield

                    # Create a new row
                    new_row = pd.DataFrame({
                        "Ticker": [ticker],
                        "Ex-Date": [ex_date],
                        "Dividend": [dividend],
                        "Closing Price On Ex-Date": [closing_price],
                        "Dividend Yield": [dividend_yield],
                        "Weighted Yield": [weighted_yield]
                    })

                    # Append the new row to the DataFrame
                    dividends_yields_df = pd.concat([dividends_yields_df, new_row], ignore_index=True)
                else:
                    print(f"No price data available for {ticker} on {ex_date}")
        else:
            print(f"{ticker}: No dividends data for 2023")
    except Exception as e:
        print(f"An error occurred for {ticker}: {e}")

# Convert 'Ex-Date' to datetime to sort by date
dividends_yields_df['Ex-Date'] = pd.to_datetime(dividends_yields_df['Ex-Date'])

# Sort the DataFrame by 'Ex-Date'
dividends_yields_df.sort_values(by='Ex-Date', inplace=True)

# Save the DataFrame to a CSV file
dividends_yields_df.to_csv("dow_dividends_weighted_yields_2023.csv", index=False)
