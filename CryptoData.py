import config
from binance import Client

# Binance API ile giriş yapıldı
# client = Client(config.API_KEY, config.API_SECRET)
client = Client()

# Tarih girilerek istenen mum bilgileri
def get_parite_list_historical(trade, interval, startDate):
    return client.get_historical_klines_generator(trade, interval, startDate)

# Limit belirtilerek istenen mum bilgileri
def get_parite_list_limit(trade, interval, limit):
    return client.get_klines(symbol=trade, interval=interval, limit=limit)

# Binance üzerindeki MARGIN işlem yapabilen USDT pariteleri
def get_symbols():
    list = client.get_exchange_info()
    ret = []
    for i in list['symbols']:
        if i['symbol'][-4:] == 'USDT' and i['symbol'][-8:] != 'DOWNUSDT' and i['symbol'][-6:] != 'UPUSDT' and 'MARGIN' in i['permissions'] and i['symbol'] != 'LENDUSDT':
            ret.append(i['symbol'])

    return ret
