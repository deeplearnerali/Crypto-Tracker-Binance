# Crypto Tracker (Binance)
## _Track Crypto Prices Through Python !_

![download](https://user-images.githubusercontent.com/47928398/174155643-5af397ee-8770-4da1-afed-b76e9ead062f.jpg)


Binance is a major crypto exchange with an API that displays crypto prices, alerts and more which we have implemented in GoodCrypto for convenience and a fun little project for beginners !


- Choose your crypto of choice
- Set minimum and maximum price alerts
- Backwards compatability with both Windows and Mac
- ✨Magic✨


This project was orginally a refactoring from a beginner
on discord who sent me his code and it was smelly! 

What I fixed:
> Redundant code
> Windows-only compatability
> Unhandled Erorr exceptions
> Messy Code
> Spelling Errors
> Hard-Static coded values


## Crypto List

GoodCrypto uses only one API and a single thread when tracking a crypto's price
So far the tool can track:
- Bitcoin
- Etherum
- Binance
- Bitcoin Cash
- Monero
- Litecoin
- Tether
- USD Coin
- Yearn Finance
- Pax Gold
- Maker
- Illuvium
- Gnosis
- Zcash


And of course GoodCrypto is free for use and distribution it's not a crazy complex thing, go modify this and have fun!

## Installation

GoodCrypto requires [python](https://python.org/) 3+ to run.

Install the dependencies run the tool!
```sh
cd CryptoTracker
pip install -r requirements.txt
python3 ./main.py or python main.py or ./main.py depending on your OS
```

## API(s) Used

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | API |
| ------ | ------ |
| Binance | [Binance API](https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT)

## How to contact me
- asyncio.me@gmail.com

