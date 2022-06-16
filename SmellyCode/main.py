# given to me by AIO on discord:
import json
import os
import requests
import winsound
import time
import threading

def start():
    print(f'''
    Choose one of the following cryptos to view thier prices
    1. Bitcoin/BTC
    2. Etherum/ETH
    3. BNB
    4. Bitcoin cash/BCH
    5. Monero/XMR
    6. Litecoin/LTC
    7. Tether/USDT
    8. USD COIN/USDC
    9. Yearn Finance/YFI
    10. Pax Gold/PAXG
    11. Maker/MKR
    12. Illuvium/ILV
    13. Gnosis/GNO
    14. Zcash/ZEC
    15. Options''')

start()

user_input = int(input("Enter a number: "))

while 69 < 420:
    if user_input == 1:
            bitcoin = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
            btc = requests.get(bitcoin)
            btc = btc.json()
            price = btc['price']
            print(f"The price of one Bitcoin is: {btc['price']}$")

            beep_money_value_btc = int(50000)
            if beep_money_value_btc > float(btc['price']):
                frequency = 2000
                duration = 690
                winsound.Beep(frequency, duration)
            os.system("cls")

while 69 < 420:
    if user_input == 2:
        etherum = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
        eth = requests.get(etherum) 
        eth = eth.json()
        os.system("title Crypto price tracker  Current price of Etherum/ETH: ")
        print(f"The price of one Etherum is: {eth['price']}$")
        time.sleep(1)
        os.system("cls")

while 69 < 420:
    if user_input == 3:
        bnb_main = "https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT"
        bnb = requests.get(bnb_main)
        bnb = bnb.json()
        os.system("title Crypto price tracker  Current price of BNB: ")
        print(f"The price of one BNB is: {bnb['price']}$")
        time.sleep(1)
        os.system("cls")

while 69 < 420:
    if user_input == 4:
        bitcoin_cash = "https://api.binance.com/api/v3/ticker/price?symbol=BCHUSDT"
        bch = requests.get(bitcoin_cash)
        bch = bch.json()
        os.system("title Crypto price tracker  Current price of Bitcoin cash/BCH: ")
        print(f"The price of one Bitcoin cash/BCH is: {bch['price']}$")
        time.sleep(1)
        os.system("cls")

while 69 < 420:
    if user_input == 5:
        monero = "https://api.binance.com/api/v3/ticker/price?symbol=XMRUSDT"
        xmr = requests.get(monero)
        xmr = xmr.json()
        os.system("title Crypto price tracker  Current price of Monero/XMR: ")
        print(f"The price of one Monero/XMR is: {xmr['price']}$")
        time.sleep(1)
        os.system("cls")

while 69 < 420:
    if user_input == 6:
        litecoin = "https://api.binance.com/api/v3/ticker/price?symbol=LTCUSDT"
        ltc = requests.get(litecoin)
        ltc = ltc.json()
        os.system("title Crypto price tracker  Current price of Litecoin/LTC: ")
        print(f"The price of one Litecoin/LTC is: {ltc['price']}$")
        time.sleep(1)
        os.system("cls")

while 69 < 420:
    if user_input == 7:
        tether = "https://api.binance.com/api/v3/ticker/price?symbol=TUSDUSDT"
        usdt = requests.get(tether)
        usdt = usdt.json()
        os.system("title Crypto price tracker  Current price of Tether/USDT: ")
        print(f"The price of one Tether/USDT is: {usdt['price']}$")
        time.sleep(1)
        os.system("cls")

while 69 < 420:
    if user_input == 8:
        usd_coin = "https://api.binance.com/api/v3/ticker/price?symbol=USDCUSDT"
        usdc = requests.get(usd_coin)
        usdc = usdc.json()
        os.system("title Crypto price tracker  Current price of USD COIN/USDC: ")
        print(f"The price of one USD COIN/USDC is: {usdc['price']}$")
        time.sleep(1)
        os.system("cls")

while 69 < 420:
    if user_input == 9:
        yearn_finance = "https://api.binance.com/api/v3/ticker/price?symbol=YFIUSDT"
        yfi = requests.get(yearn_finance)
        yfi = yfi.json()
        os.system("title Crypto price tracker  Current price of Yearn Finance/YFI: ")
        print(f"The price of one Yearn Finance/YFI is: {yfi['price']}$")
        time.sleep(1)
        os.system("cls")

while 69 < 420:
    if user_input == 10:
        pax_gold = "https://api.binance.com/api/v3/ticker/price?symbol=PAXGUSDT"
        paxg = requests.get(pax_gold)
        paxg = paxg.json()
        os.system("title Crypto price tracker  Current price of Pax Gold/PAXG: ")
        print(f"The price of one Pax Gold/PAXG is: {paxg['price']}$")
        time.sleep(1)
        os.system("cls")

while 69 < 420:
    if user_input == 11:
        maker = "https://api.binance.com/api/v3/ticker/price?symbol=MKRUSDT"
        mkr = requests.get(maker)
        mkr = mkr.json()
        os.system("title Crypto price tracker  Current price of Maker/MKR: ")
        print(f"The price of one maker/MKR is: {mkr['price']}$")
        time.sleep(1)
        os.system("cls")

while 69 < 420:
    if user_input == 12:
        Illuvium = "https://api.binance.com/api/v3/ticker/price?symbol=ILVUSDT"
        ilv = requests.get(Illuvium)
        ilv = ilv.json()
        os.system("title Crypto price tracker  Current price of Illuvium/ILV: ")
        print(f"The price of one Illuvium/ILV is: {ilv['price']}$")
        time.sleep(1)
        os.system("cls")

while 69 < 420:
    if user_input == 13:
        Gnosis = "https://api.binance.com/api/v3/ticker/price?symbol=GNOUSDT"
        gno = requests.get(Gnosis)
        gno = gno.json()
        os.system("title Crypto price tracker  Current price of Gnosis/GNO: ")
        print(f"The price of one Gnosis/GNO is: {gno['price']}$")
        time.sleep(1)
        os.system("cls")

while 69 < 420:
    if user_input == 14:
        zcash = "https://api.binance.com/api/v3/ticker/price?symbol=ZECUSDT"
        zec = requests.get(zcash)
        zec = zec.json()
        os.system("title Crypto price tracker  Current price of Zcash/ZEC: ")
        print(f"The price of one Zcash/ZEC is: {zec['price']}$")
        time.sleep(1)
        os.system("cls")

else:
    print("Invalid character/ Not a number")
    start()
