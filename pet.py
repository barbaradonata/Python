import tkinter as tk
from tkinter import messagebox

from tkinter import *
from tkinter.ttk import *

def mensagem():
    messagebox.showinfo("Tutor",f" \nNome do Tutor: {entryNome_Tutor.get()};\nNome do Pet: {entryNome_Pet.get()};\nData de Nascimento: {entryNascimento.get()}; \nEspecie: {combo.get()};\nRaça: {entryRaça.get()}")

janela = tk.Tk()
janela.title("Cadastro de Pet")

labelNome_Tutor = tk.Label(janela,text="Nome Tutor")
labelNome_Tutor.pack(padx=50, pady=5)

entryNome_Tutor = tk.Entry(janela, width=40)
entryNome_Tutor.pack(padx=50, pady=5)

labelNome_Pet = tk.Label(janela,text="Nome do Pet")
labelNome_Pet.pack(padx=50, pady=5)

entryNome_Pet = tk.Entry(janela, width=40)
entryNome_Pet.pack(padx=50, pady=5)

labelNascimento = tk.Label(janela,text="Data de Nascimento")
labelNascimento.pack(padx=50, pady=5)

entryNascimento = tk.Entry(janela, width=20)
entryNascimento.pack(padx=50, pady=5)

labelEspecie = tk.Label(janela,text="Espécie do Animal")
labelEspecie.pack(padx=50, pady=5)


combo = Combobox(janela)
combo['values']= ("Cachorro", "Gato", "Cavalo", "Outros")
combo.current(0)
combo.get ()
combo.pack(padx=50, pady=5)


labelRaça = tk.Label(janela,text="Raça do Pet")
labelRaça.pack(padx=50, pady=5)

entryRaça = tk.Entry(janela, width=30)
entryRaça.pack(padx=50, pady=5)

button_salvar = tk.Button(janela,text="Salvar",command=mensagem)
button_salvar.pack(pady=20)

janela.geometry("500x400")
janela.mainloop()