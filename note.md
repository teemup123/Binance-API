## Binance Web Socket ##
Binance base URL: wss://stream.binance.com:9443
    Append the URL with: 
        /ws/<stream_name> 
        stream name: 
            <symbol>@trade
            <symbol>@kline_<interval> - candle stick, specify time frame i.e. '1h', '1m', etc.  
Example output: 
    {"e":"kline","E":1632888202325,"s":"BTCUSDT","k":{"t":1632888000000,"T":1632888299999,"s":"BTCUSDT","i":"5m","f":1072383038,"L":1072385381,"o":"42199.99000000","c":"42161.98000000","h":"42233.84000000","l":"42149.00000000","v":"91.51234000","n":2344,"x":false,"q":"3859528.99508990","V":"45.02777000","Q":"1898922.57792450","B":"0"}}
Output meaning: check documentation: https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md#general-wss-information