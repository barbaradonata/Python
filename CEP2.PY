import tkinter as tk
from tkinter import messagebox
import requests

def buscar_cep():
    uf = entry_uf.get().strip()
    cidade = entry_cidade.get().strip()
    logradouro = entry_logradouro.get().strip()

    url = f"https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        dados = dados[0]

        if "erro" in dados:
            messagebox.showerror("Erro", "CEP não encontrado")
        else:
            endereco = (
                f"CEP: {dados['cep']}\n"
                f"Logradouro: {dados['logradouro']}\n"
                f"Bairro: {dados['bairro']}\n"
                f"Cidade: {dados['localidade']}\n"
                f"Estado: {dados['uf']}\n"
            )
            label_resultado.config(text=endereco)
    else:
        messagebox.showerror("Erro", "Erro na consulta ao ViaCep")
    
# Configurando a janela principal
root = tk.Tk()
root.title("Busca de Endereço pelo CEP")
root.geometry("300x500")

# Campo de entrada para o Estado/Cidade e Logradouro
label_uf = tk.Label(root, text="Digite o Estado:")
label_uf.pack(pady=5)
entry_uf = tk.Entry(root)
entry_uf.pack(pady=5)

label_cidade = tk.Label(root, text="Digite a Cidade:")
label_cidade.pack(pady=5)
entry_cidade = tk.Entry(root)
entry_cidade.pack(pady=5)

label_logradouro = tk.Label(root, text="Digite o Logradouro:")
label_logradouro.pack(pady=5)
entry_logradouro = tk.Entry(root)
entry_logradouro.pack(pady=5)

# Botão para buscar o endereço
botao_buscar = tk.Button(root, text="Buscar CEP", command=buscar_cep)
botao_buscar.pack(pady=10)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack(pady=10)

# Executando o loop da interface gráfica
root.mainloop()