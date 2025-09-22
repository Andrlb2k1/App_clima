# Importações
import requests
from datetime import datetime
import json
import pytz


chave = '21b05e2c5b92060ff5acf224c6da6ecd'
cidade = 'Lisboa'
api_link = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(cidade, chave)

# Fazendo a chamada da API usando request
r = requests.get(api_link)

# Convertendo os dados presentes na variável "r" em dicionário
dados = r.json()

print(dados)
print('*'*45)

# Obtendo zona, país e horas
pais_codigo = dados['sys']['country']

print(pais_codigo)

# Zona
zona_fuso = pytz.country_timezones[pais_codigo]

print(zona_fuso)

# País
pais = pytz.country_names[pais_codigo]

print(pais)

# Data
zona = pytz.timezone(zona_fuso[0])
zona_horas = datetime.now(zona)
zona_horas = zona_horas.strftime("%d %m %Y | %H:%M:%S %p")

print(zona)
print(zona_horas)

# Tempo
tempo = dados['main']['temp']
pressao = dados['main']['pressure']
umidade = dados['main']['humidity']
velocidade = dados['wind']['speed']
descricao = dados['weather'][0]['description']

print(tempo, pressao, umidade, velocidade, descricao)