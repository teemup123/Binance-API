import config, csv
from binance.client import Client

client = Client(config.API_KEY, config.API_SECRET)

csvfile = open('2021_15min_JanOct.csv', 'w', newline='') 
candlestick_writer = csv.writer(csvfile, delimiter=',')

#candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2020", "12 Jul, 2020")
candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2021", "10 Oct, 2021")
#candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2021", "10 Oct, 2021")

for candlestick in  candlesticks:
    candlestick[0] = candlestick[0] / 1000
    candlestick_writer.writerow(candlestick)

csvfile.close()