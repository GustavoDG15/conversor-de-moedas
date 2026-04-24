import requests

url = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

moedas = url.json()

dolar_real = moedas["USDBRL"]["ask"]
euro_real = moedas["EURBRL"]["ask"]
bitcoin_real = moedas["BTCBRL"]["ask"]
