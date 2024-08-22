print("Sistema de Conversão do Dólar")
print("Desenvolvido por: Bárbara Oliveira")
print("Copywrite 2024")
print("versão 1.0")

while True:
    valoremdolar = float(input("Valor do produto em dólar: "))
    cotacaodolarhoje = float(input("Digite a cotação do dólar: "))

    valorconvertido = valoremdolar * cotacaodolarhoje

    print(f"0 valor convertido de US$ {valoremdolar} é: R$ {valorconvertido}")
    sair = input("Deseja converter outro valor? <S/N>: ")
    if sair.upper() == "N":
        break
    print("Agradeço pela visita. Volte sempre. : - )")