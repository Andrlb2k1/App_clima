# Importando o Tkinter
import tkinter
from tkinter import *
from tkinter import ttk

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
janela.geometry('320x350')
janela.configure(bg=fundo)
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

# Criando os frames
frame_top = Frame(janela, width=320, height=50, bg=fundo, pady=0, padx=0)
frame_top.grid(row=1, column=0)

frame_corpo = Frame(janela, width=320, height=300, bg=fundo, pady=12, padx=0)
frame_corpo.grid(row=2, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

janela.mainloop()