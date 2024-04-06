import yfinance
from generate_symbols import get_brazilian_symbols
from datetime import datetime


end_date = datetime.now().strftime('%Y-%m-%d')
tickers = yfinance.Tickers(get_brazilian_symbols())
tickers_hist = tickers.history(period='max',end=end_date,interval='1m',)
print(tickers_hist)
