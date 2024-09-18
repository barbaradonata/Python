import tkinter as tk
from tkinter import messagebox

def mensagem():
    messagebox.showinfo("teste",f"{entryNome.get()};\ntel:{entryTelefone.get()}")

janela = tk.Tk()
janela.title("Cadastro de Cliente")

labelNome = tk.Label(janela,text="Nome")
labelNome.pack(padx=50, pady=5)

entryNome = tk.Entry(janela, width=60)
entryNome.pack(padx=50, pady=5)

labelTelefone = tk.Label(janela,text="Telefone")
labelTelefone.pack(padx=50, pady=5)

entryTelefone = tk.Entry(janela)
entryTelefone.pack(padx=50, pady=5)

labelEmail = tk.Label(janela,text="E-mail")
labelEmail.pack(padx=50, pady=5)

entryEmail = tk.Entry(janela, width=50)
entryEmail.pack(padx=50, pady=5)

button_salvar = tk.Button(janela,text="Salvar",command=mensagem)
button_salvar.pack(pady=20)

janela.geometry("400x250")
janela.mainloop()