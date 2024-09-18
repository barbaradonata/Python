estoque = ["caneta", "caderno", "borracha", "lápis"]

#Adicionar novo item ao estoque
estoque.append("marcados")
print(estoque)

#Remove item do estoque
estoque.remove("lápis")
print(estoque)

#verificar se um item está na estoque
print("borracha" in estoque) 