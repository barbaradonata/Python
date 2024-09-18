import tkinter as tk

def i_rango():
    
    quantidade = float(entry_quant.get().strip())
    preco = float(entry_preco.get().strip())
    totalpedido = (quantidade*preco)
    labeltotal.config(text=f"R$ {totalpedido:.2f}")
    return
    
#janela principal
root = tk.Tk()
root.title("Faça seu Pedido")

tk.Label(root, text="Lanche:").grid(row=0, column=0, padx=10, pady=5)
entry_lanche = tk.Entry(root)
entry_lanche.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Quantidade:").grid(row=1, column=0, padx=10, pady=5)
entry_quant = tk.Entry(root)
entry_quant.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Preço:").grid(row=2, column=0, padx=10, pady=5)
entry_preco = tk.Entry(root)
entry_preco.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Total do Pedido:").grid(row=3, column=0, padx=10, pady=5)
labeltotal = tk.Label(root)
labeltotal.grid(row=3, column=1, padx=10, pady=5)

button_calcular = tk.Button(root,text="Calcular Total",command=i_rango)
button_calcular.grid(pady=20)

root.mainloop()

    

