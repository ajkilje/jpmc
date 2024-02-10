import numpy as np
from datetime import datetime, timedelta

class ExampleAssignment_StockExchange:
    def __init__(self):
        self.trades = []
        self.stocks = {}

    def add_stock(self, symbol, stock_type, last_dividend, fixed_dividend, par_value):
        self.stocks[symbol] = {
            'Type': stock_type,
            'Last Dividend': last_dividend,
            'Fixed Dividend': fixed_dividend,
            'Par Value': par_value,
            'Prices': [],
            'Trades': []
        }

    def record_trade(self, symbol, quantity, buy_sell_indicator, price):
        trade_detail = {
                'Timestamp': datetime.now(), 
                'Stock Symbol': symbol, 
                'Quantity': quantity, 
                'Buy/Sell': buy_sell_indicator, 
                'Price': price
            }
        self.trades.append(trade_detail)
        self.stocks[symbol]['Prices'].append(price)
        self.stocks[symbol]['Trades'].append(trade_detail)

    def calculate_dividend_yield(self, symbol, price):
        stock = self.stocks[symbol]
        if stock['Type'] == 'Common':
            return stock['Last Dividend'] / price
        elif stock['Type'] == 'Preferred':
            return (stock['Fixed Dividend'] * stock['Par Value']) / price

    def calculate_pe_ratio(self, symbol, price):
        stock = self.stocks[symbol]
        return price / self.calculate_dividend_yield(symbol, price)

    def calculate_volume_weighted_stock_price(self, symbol):
        trades_in_last_15mins = [trade for trade in self.stocks[symbol]['Trades'] if trade['Timestamp'] >= datetime.now() - timedelta(minutes=15)]
        if not trades_in_last_15mins:
            return None
        total_value = sum(trade['Price'] * trade['Quantity'] for trade in trades_in_last_15mins)
        total_quantity = sum(trade['Quantity'] for trade in trades_in_last_15mins)
        return total_value / total_quantity

    def calculate_geometric_mean(self):
        prices = []
        for symbol, stock in self.stocks.items():
            prices.extend(stock['Prices'])
        return np.prod(prices) ** (1 / len(prices))

def main():
    # Sample usage
    gbce = ExampleAssignment_StockExchange()

    # adding data
    gbce.add_stock('TEA', 'Common', 0, np.nan, 100)
    gbce.add_stock('POP', 'Common', 8, np.nan, 100)
    gbce.add_stock('ALE', 'Common', 23, np.nan, 60)
    gbce.add_stock('GIN', 'Preferred', 8, 0.02, 100)
    gbce.add_stock('JOE', 'Common', 13, np.nan, 250)

    # iii. Record a trade, with timestamp, quantity of shares, buy or sell indicator and traded price
    gbce.record_trade('TEA', 10, 'Buy', 110)
    gbce.record_trade('POP', 20, 'Sell', 90)

    # i. Given any price as input, calculate the dividend yield
    print("Dividend Yield for TEA:", gbce.calculate_dividend_yield('TEA', 110))

    # ii. Given any price as input, calculate the P/E Ratio
    print("P/E Ratio for POP:", gbce.calculate_pe_ratio('POP', 90))

    # iv. Calculate Volume Weighted Stock Price based on trade in past 15mins
    print("Volume Weighted Stock Price for TEA:", gbce.calculate_volume_weighted_stock_price('TEA'))

    # b. Calculate the GBCE All Share Index using geometric mean of prices for all stocks
    print("GBCE All Share Index (Geometric Mean of Prices):", gbce.calculate_geometric_mean())
