
import backtrader as bt
import datetime


class RSIStrategy(bt.Strategy): #subclass of bt.Strategy

    def __init__(self): 
        self.rsi = bt.talib.RSI(self.data, period=14)

    def next(self):
        if self.rsi < 30 and not self.position:
            self.buy()
        
        if self.rsi > 70 and self.position:
            self.close()


       


cerebro = bt.Cerebro()

fromdate = datetime.datetime.strptime('2021-01-01', '%Y-%m-%d')
todate = datetime.datetime.strptime('2021-10-10', '%Y-%m-%d')

data = bt.feeds.GenericCSVData(dataname='2021_15min_JanOct.csv', dtformat=2, compression=1, timeframe=bt.TimeFrame.Minutes, fromdate=fromdate, todate=todate)

cerebro.adddata(data)
cerebro.broker.set_cash(1E6)
cerebro.addsizer(bt.sizers.PercentSizer, percents = 10)

cerebro.addstrategy(RSIStrategy)

cerebro.run()

cerebro.plot()