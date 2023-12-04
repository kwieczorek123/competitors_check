# Oanda
symbols_oanda = [
    "COPPER",
    "SOYBEANS", "WHEAT", "CORN",
    "SUGAR",
    "HK50", "CHINA50"
]

symbols_digits_oanda = {
    "COPPER": 4,
    "SOYBEANS": 3, "WHEAT": 3, "CORN": 3,
    "SUGAR": 4,
    "HK50": 1, "CHINA50": 1,
}

# AvaTrade
symbols_avatrade = [
    "COPPER",
    "DOLLAR_INDX",
    "SOYBEANS", "WHEAT", "CORN",
    "SUGAR#11", "COFFEE_C", "COCOA",
    "PLATINUM", "PALLADIUM",
    "HK_50", "CHINA_A50"
]

symbols_digits_avatrade = {
    "COPPER": 4,
    "DOLLAR_INDX": 3,
    "SOYBEANS": 3, "WHEAT": 3, "CORN": 3,
    "SUGAR": 4, "COFFEE_C": 2, "COCOA": 0,
    "PLATINUM": 1, "PALLADIUM": 2,
    "HK_50": 1, "CHINA_A50": 1,
}

# Forex.com
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

# IC Markets
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

# Deriv
symbols_deriv = [
    "XAUUSD", "XAGUSD",
    "EURUSD", "GBPUSD", "USDJPY", "GBPJPY", "USDCHF", "EURGBP", "AUDUSD", "NZDUSD", "USDCAD", "AUDCAD", "AUDJPY",
    "CADJPY", "CHFJPY", "EURAUD", "EURJPY", "GBPAUD", "EURCHF", "EURNZD", "EURCAD", "GBPCHF", "GBPNZD", "GBPCAD",
    "AUDCHF", "AUDNZD", "NZDJPY", "CADCHF", "NZDCAD", "NZDCHF",
    "USDMXN", "EURMXN", "GBPMXN", "EURZAR", "USDZAR", "GBPZAR", "ZARJPY",
    "WTI_OIL", "CL_BRENT", "XNGUSD",
    "US_100", "US_500", "US_30", "JP_225", "DAX_40",
    "BTCUSD", "ETHUSD", "LTCUSD", "XRPUSD", "BCHUSD"
]

symbols_digits_deriv = {
    "XAUUSD": 2, "XAGUSD": 3,
    "EURUSD": 5, "GBPUSD": 5, "USDJPY": 3, "GBPJPY": 3, "USDCHF": 5, "EURGBP": 5, "AUDUSD": 5, "NZDUSD": 5,
    "USDCAD": 5, "AUDCAD": 5, "AUDJPY": 3, "CADJPY": 3, "CHFJPY": 3, "EURAUD": 5, "EURJPY": 3, "GBPAUD": 5,
    "EURCHF": 5, "EURNZD": 5, "EURCAD": 5, "GBPCHF": 5, "GBPNZD": 5, "GBPCAD": 5, "AUDCHF": 5, "AUDNZD": 5,
    "NZDJPY": 3, "CADCHF": 5, "NZDCAD": 5, "NZDCHF": 5,
    "USDMXN": 4, "EURMXN": 4, "GBPMXN": 4, "EURZAR": 5, "USDZAR": 5, "GBPZAR": 5, "ZARJPY": 3,
    "WTI_OIL": 2, "CL_BRENT": 2, "XNGUSD": 3,
    "US_100": 1, "US_500": 1, "US_30": 1, "JP_225": 0,  "DAX_40": 1,
    "BTCUSD": 2, "ETHUSD": 2, "LTCUSD": 2, "XRPUSD": 5, "BCHUSD": 2
}

#Exness
symbols_exness = [
    "XAUUSDm", "XAGUSDm",
    "EURUSDm", "GBPUSDm", "USDJPYm", "GBPJPYm", "USDCHFm", "EURGBPm", "AUDUSDm", "NZDUSDm", "USDCADm", "AUDCADm", "AUDJPYm",
    "CADJPYm", "CHFJPYm", "EURAUDm", "EURJPYm", "GBPAUDm", "EURCHFm", "EURNZDm", "EURCADm", "GBPCHFm", "GBPNZDm", "GBPCADm",
    "AUDCHFm", "AUDNZDm", "NZDJPYm", "CADCHFm", "NZDCADm", "NZDCHFm",
    "USDMXNm", "EURMXNm", "GBPMXNm", "EURZARm", "USDZARm", "GBPZARm", "ZARJPYm",
    "USOILm", "UKOILm", "XNGUSDm",
    "USTECm", "US500m", "US30m", "JP225m", "DE30m",
    "BTCUSDm", "ETHUSDm", "LTCUSDm", "XRPUSDm", "BCHUSDm"
]

symbols_digits_exness = {
    "XAUUSDm": 2, "XAGUSDm": 3,
    "EURUSDm": 5, "GBPUSDm": 5, "USDJPYm": 3, "GBPJPYm": 3, "USDCHFm": 5, "EURGBPm": 5, "AUDUSDm": 5, "NZDUSDm": 5,
    "USDCADm": 5, "AUDCADm": 5, "AUDJPYm": 3, "CADJPYm": 3, "CHFJPYm": 3, "EURAUDm": 5, "EURJPYm": 3, "GBPAUDm": 5,
    "EURCHFm": 5, "EURNZDm": 5, "EURCADm": 5, "GBPCHFm": 5, "GBPNZDm": 5, "GBPCADm": 5, "AUDCHFm": 5, "AUDNZDm": 5,
    "NZDJPYm": 3, "CADCHFm": 5, "NZDCADm": 5, "NZDCHFm": 5,
    "USDMXNm": 4, "EURMXNm": 4, "GBPMXNm": 4, "EURZARm": 5, "USDZARm": 5, "GBPZARm": 5, "ZARJPYm": 3,
    "USOILm": 2, "UKOILm": 2, "XNGUSDm": 3,
    "USTECm": 1, "US500m": 1, "US30m": 1, "JP225m": 0,  "DE30m": 1,
    "BTCUSDm": 2, "ETHUSDm": 2, "LTCUSDm": 2, "XRPUSDm": 5, "BCHUSDm": 2
}

# FBS
symbols_fbs = [
    "XAUUSD", "XAGUSD",
    "EURUSD", "GBPUSD", "USDJPY", "GBPJPY", "USDCHF", "EURGBP", "AUDUSD", "NZDUSD", "USDCAD", "AUDCAD", "AUDJPY",
    "CADJPY", "CHFJPY", "EURAUD", "EURJPY", "GBPAUD", "EURCHF", "EURNZD", "EURCAD", "GBPCHF", "GBPNZD", "GBPCAD",
    "AUDCHF", "AUDNZD", "NZDJPY", "CADCHF", "NZDCAD", "NZDCHF",
    "USDMXN", "EURMXN", "GBPMXN", "EURZAR", "USDZAR", "GBPZAR", "ZARJPY",
    "XTIUSD", "XBRUSD", "XNGUSD",
    "US100", "US500", "US30", "JP225", "DE30",
    "BTCUSD", "ETHUSD", "LTCUSD", "XRPUSD", "BCHUSD"
]

symbols_digits_fbs = {
    "XAUUSD": 2, "XAGUSD": 3,
    "EURUSD": 5, "GBPUSD": 5, "USDJPY": 3, "GBPJPY": 3, "USDCHF": 5, "EURGBP": 5, "AUDUSD": 5, "NZDUSD": 5,
    "USDCAD": 5, "AUDCAD": 5, "AUDJPY": 3, "CADJPY": 3, "CHFJPY": 3, "EURAUD": 5, "EURJPY": 3, "GBPAUD": 5,
    "EURCHF": 5, "EURNZD": 5, "EURCAD": 5, "GBPCHF": 5, "GBPNZD": 5, "GBPCAD": 5, "AUDCHF": 5, "AUDNZD": 5,
    "NZDJPY": 3, "CADCHF": 5, "NZDCAD": 5, "NZDCHF": 5,
    "USDMXN": 4, "EURMXN": 4, "GBPMXN": 4, "EURZAR": 5, "USDZAR": 5, "GBPZAR": 5, "ZARJPY": 3,
    "XTIUSD": 2, "XBRUSD": 2, "XNGUSD": 3,
    "US100": 1, "US500": 1, "US30": 1, "JP225": 0,  "DE30": 1,
    "BTCUSD": 2, "ETHUSD": 2, "LTCUSD": 2, "XRPUSD": 5, "BCHUSD": 2
}

# XMGlobal
symbols_xm = [
    "GOLD", "SILVER",
    "EURUSD", "GBPUSD", "USDJPY", "GBPJPY", "USDCHF", "EURGBP", "AUDUSD", "NZDUSD", "USDCAD", "AUDCAD", "AUDJPY",
    "CADJPY", "CHFJPY", "EURAUD", "EURJPY", "GBPAUD", "EURCHF", "EURNZD", "EURCAD", "GBPCHF", "GBPNZD", "GBPCAD",
    "AUDCHF", "AUDNZD", "NZDJPY", "CADCHF", "NZDCAD", "NZDCHF",
    "USDMXN", "EURMXN", "GBPMXN", "EURZAR", "USDZAR", "GBPZAR", "ZARJPY",
    "OILCash", "BRENTCash", "NGASCash",
    "US100Cash", "US500Cash", "US30Cash", "JP225Cash", "GER40Cash",
    "BTCUSD", "ETHUSD", "LTCUSD", "XRPUSD", "BCHUSD"
]

symbols_digits_xm = {
    "GOLD": 2, "SILVER": 3,
    "EURUSD": 5, "GBPUSD": 5, "USDJPY": 3, "GBPJPY": 3, "USDCHF": 5, "EURGBP": 5, "AUDUSD": 5, "NZDUSD": 5,
    "USDCAD": 5, "AUDCAD": 5, "AUDJPY": 3, "CADJPY": 3, "CHFJPY": 3, "EURAUD": 5, "EURJPY": 3, "GBPAUD": 5,
    "EURCHF": 5, "EURNZD": 5, "EURCAD": 5, "GBPCHF": 5, "GBPNZD": 5, "GBPCAD": 5, "AUDCHF": 5, "AUDNZD": 5,
    "NZDJPY": 3, "CADCHF": 5, "NZDCAD": 5, "NZDCHF": 5,
    "USDMXN": 4, "EURMXN": 4, "GBPMXN": 4, "EURZAR": 5, "USDZAR": 5, "GBPZAR": 5, "ZARJPY": 3,
    "OILCash": 2, "BRENTCash": 2, "NGASCash": 3,
    "US100Cash": 1, "US500Cash": 1, "US30Cash": 1, "JP225Cash": 0,  "GER40Cash": 1,
    "BTCUSD": 2, "ETHUSD": 2, "LTCUSD": 2, "XRPUSD": 5, "BCHUSD": 2
}

# FxPro
symbols_fxpro = [
    "GOLD", "SILVER",
    "EURUSD", "GBPUSD", "USDJPY", "GBPJPY", "USDCHF", "EURGBP", "AUDUSD", "NZDUSD", "USDCAD", "AUDCAD", "AUDJPY",
    "CADJPY", "CHFJPY", "EURAUD", "EURJPY", "GBPAUD", "EURCHF", "EURNZD", "EURCAD", "GBPCHF", "GBPNZD", "GBPCAD",
    "AUDCHF", "AUDNZD", "NZDJPY", "CADCHF", "NZDCAD", "NZDCHF",
    "USDMXN", "EURMXN", "GBPMXN", "EURZAR", "USDZAR", "GBPZAR", "ZARJPY",
    "WTI", "BRENT", "NAT.GAS",
    "#USNDAQ100", "#USSPX500", "#US30", "#Japan225", "#Germany40",
    "BITCOIN", "ETHEREUM", "LITECOIN", "XRP", "BITCOINCASH"
]

symbols_digits_fxpro = {
    "GOLD": 2, "SILVER": 3,
    "EURUSD": 5, "GBPUSD": 5, "USDJPY": 3, "GBPJPY": 3, "USDCHF": 5, "EURGBP": 5, "AUDUSD": 5, "NZDUSD": 5,
    "USDCAD": 5, "AUDCAD": 5, "AUDJPY": 3, "CADJPY": 3, "CHFJPY": 3, "EURAUD": 5, "EURJPY": 3, "GBPAUD": 5,
    "EURCHF": 5, "EURNZD": 5, "EURCAD": 5, "GBPCHF": 5, "GBPNZD": 5, "GBPCAD": 5, "AUDCHF": 5, "AUDNZD": 5,
    "NZDJPY": 3, "CADCHF": 5, "NZDCAD": 5, "NZDCHF": 5,
    "USDMXN": 4, "EURMXN": 4, "GBPMXN": 4, "EURZAR": 5, "USDZAR": 5, "GBPZAR": 5, "ZARJPY": 3,
    "WTI": 2, "BRENT": 2, "NAT.GAS": 3,
    "#USNDAQ100": 1, "#USSPX500": 1, "#US30": 1, "#Japan225": 0,  "#Germany40": 1,
    "BITCOIN": 2, "ETHEREUM": 2, "LITECOIN": 2, "XRP": 5, "BITCOINCASH": 2
}