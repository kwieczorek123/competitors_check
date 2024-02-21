import pandas as pd

# Given values
equity = 1100
leverage = 2000
stop_out_level = 0.4

# Symbol mapping
symbols_data = {
    "XAUUSD": {"price": 2025, "lot_size": 100, "regular_spread": 0.3, "max_spread": 2.42},
    "XAGUSD": {"price": 22.9, "lot_size": 5000, "regular_spread": 0.036, "max_spread": 0.33},
    "EURUSD": {"price": 1.08, "lot_size": 100000, "regular_spread": 0.00015, "max_spread": 0.00165},
    "GBPUSD": {"price": 1.272, "lot_size": 100000, "regular_spread": 0.0002, "max_spread": 0.0019},
    "AUDUSD": {"price": 0.659, "lot_size": 100000, "regular_spread": 0.00013, "max_spread": 0.00175},
    "NZDUSD": {"price": 0.61, "lot_size": 100000, "regular_spread": 0.00017, "max_spread": 0.0033},
    "XTIUSD": {"price": 76.5, "lot_size": 1000, "regular_spread": 0.06, "max_spread": 0.22}
}

# Initialize an empty DataFrame to store results
results_df = pd.DataFrame(
    columns=['symbol', 'max_position', 'required_margin', 'so_equity_level', 'min_price_movement_to_get_so'])

# Loop through each symbol to calculate the metrics
for symbol, data in symbols_data.items():
    price = data['price']
    lot_size = data['lot_size']
    regular_spread = data['regular_spread']
    max_spread = data['max_spread']

    notional_value_per_lot = price * lot_size
    required_margin_per_lot = notional_value_per_lot / leverage
    max_lots_without_spread = equity / required_margin_per_lot
    equity_needed_for_max_spread_per_lot = max_spread * lot_size

    # Start with the max possible lots without considering the spread
    max_lots_with_spread = max_lots_without_spread

    # Loop to find the max lots considering the maximum spread
    while equity - (equity_needed_for_max_spread_per_lot * max_lots_with_spread) < stop_out_level * (
            required_margin_per_lot * max_lots_with_spread):
        max_lots_with_spread -= 0.01  # Decrement to find the maximum possible lots

    # Ensure the result is not negative or unrealistic
    max_position = round(max(0.0, max_lots_with_spread), 2)
    required_margin = round(required_margin_per_lot * max_position, 2)
    so_equity_level = round(required_margin * stop_out_level, 2)
    min_price_movement_to_get_so = round(max_spread / price * 100, 2)

    # Append the results to the DataFrame
    results_df = results_df._append({
        'symbol': symbol,
        'max_position': max_position,
        'required_margin': required_margin,
        'so_equity_level': so_equity_level,
        'min_price_movement_to_get_so': min_price_movement_to_get_so
    }, ignore_index=True)

# Display the resulting DataFrame
print(results_df)

# Save the DataFrame to a CSV file
csv_file_path = 'symbol_calculations_jfg.csv'
results_df.to_csv(csv_file_path, index=False)
