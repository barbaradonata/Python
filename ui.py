import tkinter as tk
from tkinter import simpledialog, messagebox

#Configuração básica da interface gráfica
root = tk.Tk()
root.withdraw()   #Esconde a janela principal

# Exemplo de uso
messagebox.showinfo("Print","Olá, mundo!") #para substituir o print
nomeDigitado = simpledialog.askstring("Input","Qual é o seu nome?")
nomeSobrenome = simpledialog.askstring("Input","Qual é o seu sobrenome?") #para inputar no sistema 
messagebox.showinfo("Print",f"Seu nome é {nomeDigitado} {nomeSobrenome}") #Caixa de saída