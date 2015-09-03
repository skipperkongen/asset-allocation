#!/usr/bin/env python
"""
How to implement this script?
- SO: http://stackoverflow.com/questions/5081710/how-to-create-a-stock-quote-fetching-app-in-python

Python modules:
- Stocks: https://pypi.python.org/pypi/yahoo-finance/
- Stocks: https://pypi.python.org/pypi/googlefinance
- Bonds: ?
"""
import sys

import yahoo_finance as yf
import googlefinance as gf

if len(sys.argv) == 1:
    print "supply at least one symbol, e.g. printinfo.py AAPL GOOG"
    sys.exit()

print "Printing info for symbols v.0.1"
print ""

for symbol in sys.argv[1:]:
    print "{0}: Fetching info from Yahoo".format(symbol)
    stock = yf.Share(symbol)
    print "................................."
    print "Overview:"
    for key, value in stock.get_info().items():
        print "  {0}: {1}".format(key, value)
    print "  Stock exchange: " + stock.get_stock_exchange()
    print "  Market cap: " + stock.get_market_cap()
    print "Pricing:"
    print "  Price earnings ratio: " + stock.get_price_earnings_ratio()
    print "  Price earnings growth ratio: " + stock.get_price_earnings_growth_ratio()
    print "  Open: " + stock.get_open()
    print "  Price: " + stock.get_price()
    print "  Change: " + stock.get_change()
    print "  Days high: " + stock.get_days_high()
    print "  Days low: " + stock.get_days_low()
    print "  Year high: " + stock.get_year_high()
    print "  Year low: " + stock.get_year_low()
    print "  50 day moving avg: " + stock.get_50day_moving_avg()
    print "  200 day moving avg: " + stock.get_200day_moving_avg()

    print ""
    continue
    print "Volume: " + stock.get_volume()
    print "Prev close: " + stock.get_prev_close()
    print "Avg. daily volume: " + stock.get_avg_daily_volume()
    print "Book value: " + stock.get_book_value()
    print "Ebitda: " + stock.get_ebitda()
    print "Dividend share: " + stock.get_dividend_share()
    print "Dividend yield: " + stock.get_dividend_yield()
    print "Earnings share: " + stock.get_earnings_share()
    print "Price sales: " + stock.get_price_sales()
    print "Price book: " + stock.get_price_book()
    print "Short ratio: " + stock.get_short_ratio()
    print "Trade datatime: " + stock.get_trade_datetime()
    print ""
	#print "" + stock.get_historical(start_date, end_date)
