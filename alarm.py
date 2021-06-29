import time
import talib
import numpy as np
import CryptoData as cd
from talib import MA_Type
import telegram_bot as tbot
from datetime import datetime

# binance_symbols = cd.get_symbols()
symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'ADAUSDT', 'DOGEUSDT', 'XRPUSDT', 'DOTUSDT',
           'UNIUSDT', 'LTCUSDT', 'SOLUSDT', 'LINKUSDT', 'MATICUSDT', 'THETAUSDT', 'XLMUSDT',
           'VETUSDT', 'ETCUSDT', 'TRXUSDT', 'FILUSDT', 'XMRUSDT', 'EOSUSDT',
           'AAVEUSDT', 'ALGOUSDT', 'XTZUSDT', 'NEOUSDT', 'MKRUSDT', 'ATOMUSDT',
           'AVAXUSDT', 'KSMUSDT', 'BTTUSDT', 'GRTUSDT', 'COMPUSDT', 'HBARUSDT', 'RUNEUSDT',
           'WAVESUSDT', 'CHZUSDT', 'ZECUSDT', 'DASHUSDT', 'EGLDUSDT', 'YFIUSDT',
           'XEMUSDT', 'SUSHIUSDT', 'ZILUSDT', 'BATUSDT', 'ENJUSDT',
           'NEARUSDT', 'MANAUSDT', 'SNXUSDT', 'ONEUSDT', 'DGBUSDT', 'QTUMUSDT',
           'CRVUSDT', 'ZRXUSDT', 'SCUSDT', 'FTMUSDT', 'ONTUSDT', 'OMGUSDT', 'ANKRUSDT',
           'RVNUSDT', '1INCHUSDT', 'LRCUSDT', 'IOSTUSDT', 'RSRUSDT',
           'KNCUSDT', 'OCEANUSDT', 'KAVAUSDT', 'RLCUSDT', 'SKLUSDT', 'OGNUSDT',
           'REEFUSDT', 'STORJUSDT', 'BANDUSDT', 'SXPUSDT', 'STMXUSDT', 'NKNUSDT', 'CELRUSDT',
           'SRMUSDT', 'SANDUSDT', 'BTSUSDT', 'BALUSDT', 'ALPHAUSDT', 'TOMOUSDT']

print("İşlem başlatıldı...")


while True:
    now = datetime.now()
    if now.minute % 5 == 0:
        print("LOG: Sorgulama başladı!")
        for symbol in symbols:
            print("LOG:", symbol, "paritesi inceleniyor.")
            try:
                data = cd.get_parite_list_limit(symbol, cd.client.KLINE_INTERVAL_5MINUTE, 300)
                data = np.array(data)
                data = data.astype(np.float64)
                data_close = data[:,4] # Kriptoya ait 4 saatlik kapanış fiyatları
                data_high = data[:,2] # Kriptoya ait 4 saatlik en yüksek fiyatlar
                data_low = data[:,3] # Kriptoya ait 4 saatlik en düşük fiyatlar

                data4h = cd.get_parite_list_limit(symbol, cd.client.KLINE_INTERVAL_4HOUR, 300)
                data4h = np.array(data4h)
                data4h = data4h.astype(np.float64)
                data_close4h = data4h[:,4] # Kriptoya ait 4 saatlik kapanış fiyatları

                ma50 = talib.MA(data_close4h, timeperiod=50, matype=0)  # GOLDEN CROSS & DEATH CROSS (tamamlandı)
                ma200 = talib.MA(data_close4h, timeperiod=200, matype=0)  # GOLDEN CROSS & DEATH CROSS (tamamlandı)
                rsi = talib.RSI(data_close, timeperiod=14)
                bb_upper, bb_middle, bb_lower = talib.BBANDS(data_close, matype=MA_Type.T3)  # BB (Bolinger Bands) (tamamlandı)
                #fastk, fastd = talib.STOCHRSI(data_close, timeperiod=14, fastk_period=3, fastd_period=3, fastd_matype=0)  # STOCHRSI (Stochastic RSI) (tamamlandı)
                slowk, slowd = talib.STOCH(data_high, data_low, data_close, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)

                message = "*" + symbol + "*"
                messageSend = False

                 # STOCHRSI (Stochastic RSI) (tamamlandı ama ikinci koşullar silinebilir)
                if slowk[-1] >= 85 and slowd[-1] >= 85 and slowk[-1] < slowd[-1]:
                    message = message + "\n⏬ *Sinyal Tipi:* STOCHRSI Aşağı Kesti!!"
                    messageSend = True
                elif slowk[-1] <= 15 and slowd[-1] <= 15 and slowk[-1] > slowd[-1]:
                    message = message + "\n⏫ *Sinyal Tipi:* STOCHRSI Yukarı Kesti!!"
                    messageSend = True
                ###########################

                # GOLDEN and DEATH CROSS
                if ma50[-3] >= ma200[-3] and ma50[-2] >= ma200[-2] and ma50[-1] < ma200[-1]:
                    message = message + "\n☠ *Sinyal Tipi:* DEATH CROSS!!"
                    messageSend = True
                elif ma50[-3] <= ma200[-3] and ma50[-2] <= ma200[-2] and ma50[-1] > ma200[-1]:
                    message = message + "\n🥇 *Sinyal Tipi:* GOLDEN CROSS!!"
                    messageSend = True
                ###########################

                # RSI
                if rsi[-1] < 25:
                    message = message + "\n🔴 *Sinyal Tipi:* RSI AŞIRI SATIM!!\n*RSI:* " + str(rsi[-1])
                    messageSend = True
                elif rsi[-1] > 75:
                    message = message + "\n🟡 *Sinyal Tipi:* RSI AŞIRI ALIM!!\n*RSI:* " + str(rsi[-1])
                    messageSend = True
                ###########################

                #Bollinger Bandın ekle
                if data_close[-1] <= bb_lower[-1]: # alt banda geldi yukarı gidebilir
                    message = message + "\n📉 *Sinyal Tipi:* BOL.BANDI ALT SINIRDA!!"
                    messageSend = True
                elif data_close[-1] >= bb_upper[-1]: # üst banda geldi aşağı inebilir
                    message = message + "\n📈 *Sinyal Tipi:* BOL.BANDI ÜST SINIRDA!!"
                    messageSend = True
                ###########################

                message = message + "\n*Son belirlenen fiyat:* " + str(data_close[-1]) + "$\n*Sinyal Tarihi:* " + datetime.now().strftime("%d %b %Y, %H:%M")
                message = message + "\n*Tradingview Link:* [" + symbol + "](https://tr.tradingview.com/chart/?symbol=BINANCE%3A" + symbol + ")"
                message = message + "\n*Binance Link:* [" + symbol + "](https://www.binance.com/en/futures/" + symbol + ")"

                if messageSend:
                    print("LOG:", symbol, 'e ait sinyal telegramda paylaşıldı!')
                    tbot.SendMessage(message)
                    messageSend = False

                time.sleep(2)
            except ValueError:
                    print(symbol, "-> Mesaj gönderilir iken bir hata meydana geldi!!\nHata nedeni:", ValueError)
