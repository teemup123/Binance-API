import backtrader as bt 
import datetime

from backtrader import cerebro


class SimpAvgCross(bt.Strategy): 

    def __init__(self): 

        self.SimpAvg20 = bt.talib.MA(self.data, timeperiod = 20)
        self.SimpAvg7 =  bt.talib.MA(self.data, timeperiod = 7)

    def next(self): 

        if self.SimpAvg7 > self.SimpAvg20 and not self.position:
             self.buy()

        if self.SimpAvg20 > self.SimpAvg7 and self.position: 
            self.close()

cerebro = bt.Cerebro()

fromdate = datetime.datetime.strptime('2021-10-01', '%Y-%m-%d')
todate = datetime.datetime.strptime('2021-10-11', '%Y-%m-%d')

data = bt.feeds.GenericCSVData(dataname='2021_15min_JanOct.csv', dtformat=2, compression=1, timeframe=bt.TimeFrame.Minutes, fromdate=fromdate, todate=todate)

cerebro.adddata(data)
cerebro.broker.set_cash(1E6)
cerebro.addsizer(bt.sizers.PercentSizer, percents = 50)

cerebro.addstrategy(SimpAvgCross)

cerebro.run()

cerebro.plot()