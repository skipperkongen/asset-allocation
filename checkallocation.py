#!/usr/bin/env python
"""
How to implement this script?
- SO: http://stackoverflow.com/questions/5081710/how-to-create-a-stock-quote-fetching-app-in-python

Python modules:
- Stocks: https://pypi.python.org/pypi/yahoo-finance/
- Stocks: https://pypi.python.org/pypi/googlefinance
- Bonds: ?
"""
import yahoo_finance as yf
import googlefinance as gf

print "Asset allocation script v.0.1"

# Test Yahoo
print "Getting Apple stock from Yahoo"
apple = yf.Share("AAPL")
print "Info " + str(apple.get_info())
print "Open: " + apple.get_open()
print "Price: " + apple.get_price()
print "Change: " + apple.get_change()
print "Volume: " + apple.get_volume()
print "Prev close: " + apple.get_prev_close()
print "Avg. daily volume: " + apple.get_avg_daily_volume()
print "Stock exchange: " + apple.get_stock_exchange()
print "Market cap: " + apple.get_market_cap()
print "Book value: " + apple.get_book_value()
print "Ebitda: " + apple.get_ebitda()
print "Dividend share: " + apple.get_dividend_share()
print "Dividend yield: " + apple.get_dividend_yield()
print "Earnings share: " + apple.get_earnings_share()
print "Days high: " + apple.get_days_high()
print "Days low: " + apple.get_days_low()
print "Year high: " + apple.get_year_high()
print "Year low: " + apple.get_year_low()
print "50 day moving avg: " + apple.get_50day_moving_avg()
print "200 day moving avg: " + apple.get_200day_moving_avg()
print "Price earnings ratio: " + apple.get_price_earnings_ratio()
print "Price earnings growth ratio: " + apple.get_price_earnings_growth_ratio()
print "Price sales: " + apple.get_price_sales()
print "Price book: " + apple.get_price_book()
print "Short ratio: " + apple.get_short_ratio()
print "Trade datatime: " + apple.get_trade_datetime()
#print "" + apple.get_historical(start_date, end_date)
