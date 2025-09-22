import requests
import datetime
import json

chave = '21b05e2c5b92060ff5acf224c6da6ecd'
api_link = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={}'.format(chave)

# Fazendo a chamada da API usando request
r = requests.get(api_link)

# Convertendo os dados presentes na variável "r" em dicionário
dados = r.json()

print(dados)