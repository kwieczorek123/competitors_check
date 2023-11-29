symbols = [
    "XAUUSD", "XAGUSD",
    "EURUSD", "GBPUSD", "USDJPY", "GBPJPY", "USDCHF", "EURGBP", "AUDUSD", "NZDUSD", "USDCAD", "AUDCAD", "AUDJPY",
    "CADJPY", "CHFJPY", "EURAUD", "EURJPY", "GBPAUD", "EURCHF", "EURNZD", "EURCAD", "GBPCHF", "GBPNZD", "GBPCAD",
    "AUDCHF", "AUDNZD", "NZDJPY", "CADCHF", "NZDCAD", "NZDCHF",
    "USDMXN", "EURMXN", "GBPMXN", "EURZAR", "USDZAR", "GBPZAR", "ZARJPY",
    "XTIUSD", "XBRUSD", "XNGUSD",
    "NAS100", "SPX500", "US30", "JPN225", "GER40",
    "BTCUSD", "ETHUSD", "LTCUSD", "XRPUSD", "BCHUSD"
]

symbols_digits = {
    "XAUUSD": 2, "XAGUSD": 3,
    "EURUSD": 5, "GBPUSD": 5, "USDJPY": 3, "GBPJPY": 3, "USDCHF": 5, "EURGBP": 5, "AUDUSD": 5, "NZDUSD": 5,
    "USDCAD": 5, "AUDCAD": 5, "AUDJPY": 3, "CADJPY": 3, "CHFJPY": 3, "EURAUD": 5, "EURJPY": 3, "GBPAUD": 5,
    "EURCHF": 5, "EURNZD": 5, "EURCAD": 5, "GBPCHF": 5, "GBPNZD": 5, "GBPCAD": 5, "AUDCHF": 5, "AUDNZD": 5,
    "NZDJPY": 3, "CADCHF": 5, "NZDCAD": 5, "NZDCHF": 5,
    "USDMXN": 4, "EURMXN": 4, "GBPMXN": 4, "EURZAR": 5, "USDZAR": 5, "GBPZAR": 5, "ZARJPY": 3,
    "XTIUSD": 2, "XBRUSD": 2, "XNGUSD": 3,
    "NAS100": 1, "SPX500": 1, "US30": 1, "JPN225": 0,  "GER40": 1,
    "BTCUSD": 2, "ETHUSD": 2, "LTCUSD": 2, "XRPUSD": 5, "BCHUSD": 2
}


# Oanda
symbols_oanda = [
    "XAUUSD.sml", "XAGUSD",
    "EURUSD.sml", "GBPUSD.sml", "USDJPY.sml", "GBPJPY.sml", "USDCHF", "EURGBP.sml", "AUDUSD.sml", "NZDUSD", "USDCAD",
    "AUDCAD", "AUDJPY", "CADJPY", "CHFJPY", "EURAUD", "EURJPY", "GBPAUD", "EURCHF", "EURNZD", "EURCAD", "GBPCHF",
    "GBPNZD", "GBPCAD", "AUDCHF", "AUDNZD", "NZDJPY", "CADCHF", "NZDCAD", "NZDCHF",
    "USDMXN",  "EURMXN",  "GBPMXN", "EURZAR",  "USDZAR",  "GBPZAR",  "ZARJPY",
    "USOIL.sml", "UKOIL.sml", "NATGAS",
    "US100", "US500", "US30", "JP225", "GER30.sml",
    "BTCUSD", "ETHUSD", "LTCUSD", "XRPUSD", "BCHUSD"
]


symbols_digits_oanda = {
    "XAUUSD.sml": 2, "XAGUSD": 3,
    "EURUSD.sml": 5, "GBPUSD.sml": 5, "USDJPY.sml": 3, "GBPJPY.sml": 3, "USDCHF": 5, "EURGBP.sml": 5, "AUDUSD.sml": 5,
    "NZDUSD": 5, "USDCAD": 5, "AUDCAD": 5, "AUDJPY": 3, "CADJPY": 3, "CHFJPY": 3, "EURAUD": 5, "EURJPY": 3, "GBPAUD": 5,
    "EURCHF": 5, "EURNZD": 5, "EURCAD": 5, "GBPCHF": 5, "GBPNZD": 5, "GBPCAD": 5, "AUDCHF": 5, "AUDNZD": 5,
    "NZDJPY": 3, "CADCHF": 5, "NZDCAD": 5, "NZDCHF": 5,
    "USDMXN": 4, "EURMXN": 4, "GBPMXN": 4, "EURZAR": 5, "USDZAR": 5, "GBPZAR": 5, "ZARJPY": 3,
    "USOIL.sml": 2, "UKOIL.sml": 2, "NATGAS": 3,
    "US100": 1, "US500": 1, "US30": 1, "JP225": 0,  "GER30.sml": 1,
    "BTCUSD": 2, "ETHUSD": 2, "LTCUSD": 2, "XRPUSD": 5, "BCHUSD": 2
}


# Oanda
symbols_avatrade = [
    "GOLD", "SILVER",
    "EURUSD", "GBPUSD", "USDJPY", "GBPJPY", "USDCHF", "EURGBP", "AUDUSD", "NZDUSD", "USDCAD", "AUDCAD", "AUDJPY",
    "CADJPY", "CHFJPY", "EURAUD", "EURJPY", "GBPAUD", "EURCHF", "EURNZD", "EURCAD", "GBPCHF", "GBPNZD", "GBPCAD",
    "AUDCHF", "AUDNZD", "NZDJPY", "CADCHF", "NZDCAD", "NZDCHF",
    "USDMXN", "EURMXN", "GBPMXN", "EURZAR", "USDZAR", "GBPZAR", "ZARJPY",
    "CrudeOIL", "BRENT_OIL", "NATURAL_GAS",
    "US_TECH100", "US_500", "US_30", "NIKKEI225", "DAX30",
    "BTCUSD", "ETHUSD", "LTCUSD", "XRPUSD", "BCHUSD"
]


symbols_digits_avatrade = {
    "GOLD": 2, "SILVER": 3,
    "EURUSD": 5, "GBPUSD": 5, "USDJPY": 3, "GBPJPY": 3, "USDCHF": 5, "EURGBP": 5, "AUDUSD": 5, "NZDUSD": 5,
    "USDCAD": 5, "AUDCAD": 5, "AUDJPY": 3, "CADJPY": 3, "CHFJPY": 3, "EURAUD": 5, "EURJPY": 3, "GBPAUD": 5,
    "EURCHF": 5, "EURNZD": 5, "EURCAD": 5, "GBPCHF": 5, "GBPNZD": 5, "GBPCAD": 5, "AUDCHF": 5, "AUDNZD": 5,
    "NZDJPY": 3, "CADCHF": 5, "NZDCAD": 5, "NZDCHF": 5,
    "USDMXN": 4, "EURMXN": 4, "GBPMXN": 4, "EURZAR": 5, "USDZAR": 5, "GBPZAR": 5, "ZARJPY": 3,
    "CrudeOIL": 2, "BRENT_OIL": 2, "NATURAL_GAS": 3,
    "US_TECH100": 1, "US_500": 1, "US_30": 1, "NIKKEI225": 0,  "DAX30": 1,
    "BTCUSD": 2, "ETHUSD": 2, "LTCUSD": 2, "XRPUSD": 5, "BCHUSD": 2
}


symbols_forexcom = [
    "XAUUSD", "XAGUSD",
    "EURUSD", "GBPUSD", "USDJPY", "GBPJPY", "USDCHF", "EURGBP", "AUDUSD", "NZDUSD", "USDCAD", "AUDCAD", "AUDJPY",
    "CADJPY", "CHFJPY", "EURAUD", "EURJPY", "GBPAUD", "EURCHF", "EURNZD", "EURCAD", "GBPCHF", "GBPNZD", "GBPCAD",
    "AUDCHF", "AUDNZD", "NZDJPY", "CADCHF", "NZDCAD", "NZDCHF",
    "USDMXN", "EURMXN", "GBPMXN", "EURZAR", "USDZAR", "GBPZAR", "ZARJPY",
    "US Oil", "UK Oil", "US Natural Gas",
    "NAS100", "SPX500", "US30", "JPN225", "GER40",
    "Bitcoin", "Ethereum", "LTCUSD", "Ripple", "BCHUSD"
]

symbols_digits_forexcom = {
    "XAUUSD": 2, "XAGUSD": 3,
    "EURUSD": 5, "GBPUSD": 5, "USDJPY": 3, "GBPJPY": 3, "USDCHF": 5, "EURGBP": 5, "AUDUSD": 5, "NZDUSD": 5,
    "USDCAD": 5, "AUDCAD": 5, "AUDJPY": 3, "CADJPY": 3, "CHFJPY": 3, "EURAUD": 5, "EURJPY": 3, "GBPAUD": 5,
    "EURCHF": 5, "EURNZD": 5, "EURCAD": 5, "GBPCHF": 5, "GBPNZD": 5, "GBPCAD": 5, "AUDCHF": 5, "AUDNZD": 5,
    "NZDJPY": 3, "CADCHF": 5, "NZDCAD": 5, "NZDCHF": 5,
    "USDMXN": 4, "EURMXN": 4, "GBPMXN": 4, "EURZAR": 5, "USDZAR": 5, "GBPZAR": 5, "ZARJPY": 3,
    "US Oil": 2, "UK Oil": 2, "US Natural Gas": 3,
    "NAS100": 1, "SPX500": 1, "US30": 1, "JPN225": 0,  "GER40": 1,
    "Bitcoin": 2, "Ethereum": 2, "LTCUSD": 2, "Ripple": 5, "BCHUSD": 2
}


symbols_icmarkets = [
    "XAUUSD", "XAGUSD",
    "EURUSD", "GBPUSD", "USDJPY", "GBPJPY", "USDCHF", "EURGBP", "AUDUSD", "NZDUSD", "USDCAD", "AUDCAD", "AUDJPY",
    "CADJPY", "CHFJPY", "EURAUD", "EURJPY", "GBPAUD", "EURCHF", "EURNZD", "EURCAD", "GBPCHF", "GBPNZD", "GBPCAD",
    "AUDCHF", "AUDNZD", "NZDJPY", "CADCHF", "NZDCAD", "NZDCHF",
    "USDMXN", "EURMXN", "GBPMXN", "EURZAR", "USDZAR", "GBPZAR", "ZARJPY",
    "XTIUSD", "XBRUSD", "XNGUSD",
    "USTEC", "US500", "US30", "JPN225", "GER40",
    "BTCUSD", "ETHUSD", "LTCUSD", "XRPUSD", "BCHUSD"
]

symbols_digits_icmarkets = {
    "XAUUSD": 2, "XAGUSD": 3,
    "EURUSD": 5, "GBPUSD": 5, "USDJPY": 3, "GBPJPY": 3, "USDCHF": 5, "EURGBP": 5, "AUDUSD": 5, "NZDUSD": 5,
    "USDCAD": 5, "AUDCAD": 5, "AUDJPY": 3, "CADJPY": 3, "CHFJPY": 3, "EURAUD": 5, "EURJPY": 3, "GBPAUD": 5,
    "EURCHF": 5, "EURNZD": 5, "EURCAD": 5, "GBPCHF": 5, "GBPNZD": 5, "GBPCAD": 5, "AUDCHF": 5, "AUDNZD": 5,
    "NZDJPY": 3, "CADCHF": 5, "NZDCAD": 5, "NZDCHF": 5,
    "USDMXN": 4, "EURMXN": 4, "GBPMXN": 4, "EURZAR": 5, "USDZAR": 5, "GBPZAR": 5, "ZARJPY": 3,
    "XTIUSD": 2, "XBRUSD": 2, "XNGUSD": 3,
    "USTEC": 1, "US500": 1, "US30": 1, "JPN225": 0,  "GER40": 1,
    "BTCUSD": 2, "ETHUSD": 2, "LTCUSD": 2, "XRPUSD": 5, "BCHUSD": 2
}