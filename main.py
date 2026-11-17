import requests

r = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")

cotacao = r.json()

cotacao["USDBRL"]["ask"]