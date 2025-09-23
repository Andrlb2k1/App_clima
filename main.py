# Importando o Tkinter
import tkinter
from tkinter import *
from tkinter import ttk

# Importando o Pillow
from PIL import Image, ImageTk

# Outras importações
import requests
from datetime import datetime
import json
import pytz
import pycountry_convert as pc

# Cores
co0 = "#444466"  # Preta
co1 = "#feffff"  # Branca
co2 = "#6f9fbd"  # Azul

fundo_dia = "#6cc4cc"
fundo_noite = "#484f60"
fundo_tarde = "#bfb86d"

fundo = fundo_dia

# Criando janela
janela = Tk()
janela.title('')
janela.geometry('330x350')
janela.configure(bg=fundo)
janela.resizable(width=FALSE, height=FALSE)
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

# Criando os frames
frame_top = Frame(janela, width=330, height=50, bg=co1, pady=0, padx=0)
frame_top.grid(row=1, column=0)

frame_corpo = Frame(janela, width=330, height=300, bg=fundo, pady=12, padx=0)
frame_corpo.grid(row=2, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

global imagem

# Função que retorna as informações
def informacao():
    chave = '21b05e2c5b92060ff5acf224c6da6ecd'
    cidade = e_local.get()
    api_link = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(cidade, chave)

    # Fazendo a chamada da API usando request
    r = requests.get(api_link)

    # Convertendo os dados presentes na variável "r" em dicionário
    dados = r.json()

    print(dados)

    # Obtendo zona, país e horas
    pais_codigo = dados['sys']['country']

    # Zona
    zona_fuso = pytz.country_timezones[pais_codigo]

    # País
    pais = pytz.country_names[pais_codigo]

    # Data
    zona = pytz.timezone(zona_fuso[0])
    zona_horas = datetime.now(zona)
    zona_horas = zona_horas.strftime("%d %m %Y | %H:%M:%S %p")

    # Tempo
    tempo = dados['main']['temp']
    pressao = dados['main']['pressure']
    umidade = dados['main']['humidity']
    velocidade = dados['wind']['speed']
    descricao = dados['weather'][0]['description']

    # Mudando informações
    def pais_para_continente(i):
        pais_alpha = pc.country_name_to_country_alpha2(i)
        pais_continente_codigo = pc.country_alpha2_to_continent_code(pais_alpha)
        pais_continente_nome = pc.convert_continent_code_to_continent_name(pais_continente_codigo)

        return pais_continente_nome

    continente = pais_para_continente(pais)

    # Passando informações nas Labels
    l_cidade['text'] = cidade + ' - ' + pais + ' / ' + continente
    l_data['text'] = zona_horas
    l_umidade['text'] = umidade
    l_u_simbolo['text'] = '%'
    l_u_nome['text'] = 'Umidade'
    l_pressao['text'] = 'Pressão : ' + str(pressao)
    l_velocidade['text'] = 'Velocidade do vento : ' + str(velocidade)
    l_descricao['text'] = descricao

    # Lógica para trocar o fundo
    zona_periodo = datetime.now(zona)
    zona_periodo = zona_periodo.strftime('%H')

    global imagem

    zona_periodo = int(zona_periodo)

    if zona_periodo <= 5:
        imagem = Image.open('images/lua.png')
        fundo = fundo_noite
    elif zona_periodo <= 11:
        imagem = Image.open('images/sol_dia.png')
        fundo = fundo_dia
    elif zona_periodo <= 17:
        imagem = Image.open('images/sol_tarde.png')
        fundo = fundo_tarde
    elif zona_periodo <= 23:
        imagem = Image.open('images/lua.png')
        fundo = fundo_noite
    else:
        pass
    
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)

    l_icone = Label(frame_corpo, image=imagem, bg=fundo)
    l_icone.place(x=162, y=50)

    # Passando informações nas Labels
    janela.configure(bg=fundo)
    frame_top.configure(bg=fundo)
    frame_corpo.configure(bg=fundo)

    l_cidade['bg'] = fundo
    l_data['bg'] = fundo
    l_umidade['bg'] = fundo
    l_u_simbolo['bg'] = fundo
    l_u_nome['bg'] = fundo
    l_pressao['bg'] = fundo
    l_velocidade['bg'] = fundo
    l_descricao['bg'] = fundo

# Configurando o frame_top
e_local = Entry(frame_top, width=20, justify='left', font=("", 14), highlightthickness=1, relief='solid')
e_local.place(x=15, y=10)

b_ver = Button(frame_top, command=informacao, text='Ver clima', bg=co1, fg=co2, font=("Ivy 9 bold"), relief='raised', overrelief=RIDGE)
b_ver.place(x=250, y=10)

# Configurando o frame_corpo
l_cidade = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=co1, font=("Arial 14"))
l_cidade.place(x=10, y=4)

l_data = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=co1, font=("Arial 10"))
l_data.place(x=10, y=54)

l_umidade = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=co1, font=("Arial 45"))
l_umidade.place(x=10, y=100)

l_u_simbolo = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=co1, font=("Arial 10 bold"))
l_u_simbolo.place(x=85, y=110)

l_u_nome = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=co1, font=("Arial 8"))
l_u_nome.place(x=85, y=140)

l_pressao = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=co1, font=("Arial 10"))
l_pressao.place(x=10, y=184)

l_velocidade = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=co1, font=("Arial 10"))
l_velocidade.place(x=10, y=212)

l_descricao = Label(frame_corpo, text='', anchor='center', bg=fundo, fg=co1, font=("Arial 10"))
l_descricao.place(x=170, y=190)

janela.mainloop()