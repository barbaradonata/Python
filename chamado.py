import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# Função para salvar o pedido em um arquivo JSON
def gerar_chamado():
    nome_cliente = entry_nome.get()
    tipo_problema = entry_tipo.get()
    descricao_problema = entry_descricao.get()
    prioridade = entry_prioridade.get()
    data = data.get()
    numchamado = numchamado.get()

    if not nome_cliente or not tipo_problema or not descricao_problema or not prioridade or not data or not numero_chamado:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    try:
        quantidade = int(quantidade)
        preco_unitario = float(preco_unitario)
    except ValueError:
        messagebox.showerror("Erro", "Quantidade deve ser número inteiro e preço deve ser um número!")
        return


    # Estrutura do pedido
    pedido = {
        "nome_cliente": nome_cliente,
        "tipo_problema": tipo_problema,
        "descricao_problema": descricao_problema,
        "prioridade": prioridade,
        "data": data,
        "numchamado": numchamado,
    }

    # Verifica se o arquivo JSON já existe
    if os.path.exists("chamado.json"):
        with open("chamado.json", "r") as arquivo:
            numchamados = json.load(arquivo)
    else:
        chamado = []

    # Adiciona o novo pedido
    chamado.append(chamado)

    # Salva no arquivo JSON
    with open("chamado.json", "w") as arquivo:
        json.dump(chamado, arquivo, indent=4)

    messagebox.showinfo("Sucesso", "Chamado salvo com sucesso!")

    # Limpa os campos após salvar
    limpar_campos()

# Função para exibir um pedido específico
def recuperar_pedido():
    if os.path.exists("chamado.json"):
        numchamado = simpledialog.askfloat("Recuperar Chamado", "Digite o número do chamado:")
        if not numchamado:
            return

        with open("chamado.json", "r") as arquivo:
            chamado = json.load(arquivo)

        # Procura o pedido pelo nome do lanche
        for chamado in chamado:
            if cliente["nome_cliente"].lower() == nome_cliente.lower():
                entry_nome.delete(0, tk.END)
                entry_nome.insert(0, cliente["nome_cliente"])
                entry_quantidade.delete(0, tk.END)
                entry_quantidade.insert(0, pedido["quantidade"])
                entry_preco.delete(0, tk.END)
                entry_preco.insert(0, pedido["preco_unitario"])
                label_total_valor.config(text=f"R$ {pedido['preco_total']:.2f}")
                return

        messagebox.showinfo("Pedido não encontrado", f"Pedido com nome '{nome_lanche}' não encontrado.")
    else:
        messagebox.showinfo("Sem Pedidos", "Nenhum pedido cadastrado até o momento.")

# Função para limpar os campos
def limpar_campos():
    entry_cliente.delete(0, tk.END)
    entry_tipo.delete(0, tk.END)
    entry_descricao.delete(0, tk.END)
    entry_data.delete(0, tk.END)
    entry_numchamado.delete(0, tk.END)
    label_total_valor.config(text="R$ 0.00")
    entry_nome.focus()

# Interface gráfica com Tkinter
janela = tk.Tk()
janela.title("Sistema de Chamados")

# Labels e Entries para os campos
label_nome = tk.Label(janela, text="Cliente")
label_nome.grid(row=0, column=0)

entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1)

#REVER
label_tipo = tk.Label(janela, text="Tipo de Problema")
label_tipo.grid(row=1, column=0)

entry_tipo = tk.Entry(janela)
entry_tipo.grid(row=1, column=1)

label_descricao = tk.Label(janela, text="Descreva o problema")
label_descricao.grid(row=2, column=0)

entry_descricao = tk.Entry(janela)
entry_descricao.grid(row=2, column=1)

# Label para exibir o total do pedido
label_prioridade = tk.Label(janela, text="Prioridade")
label_prioridade.grid(row=3, column=0)

#verificar esse
label_prioridade = tk.Entry(janela, text="Prioridade")
label_prioridade.grid(row=3, column=1)

label_numchamado = tk.Label(janela, text="Descreva o problema")
label_numchamado.grid(row=4, column=0)

entry_numchamado = tk.Entry(janela)
entry_numchamado.grid(row=4, column=1)

# Botões organizados em duas linhas


botao_gerar_chamado = tk.Button(janela, text="Gerar Chamado", width=20, command=gerar_chamado)
botao_gerar_chamado.grid(row=4, column=1)

botao_recuperar = tk.Button(janela, text="Recuperar Pedido", width=20, command=recuperar_pedido)
botao_recuperar.grid(row=5, column=0)

botao_novo_pedido = tk.Button(janela, text="Novo Pedido", width=20, command=limpar_campos)
botao_novo_pedido.grid(row=5, column=1)

janela.mainloop()