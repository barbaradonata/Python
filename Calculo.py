#numero1 = float(input("Digite o 1º número: "))
#numero2 = float(input("Digite o 2º número: "))
#resultado = numero1+numero2
#print("o resultado é ", resultado)

rodar = "S" 
#while rodar == "S" or rodar == "s":
while rodar.upper() == "S":
    operacao = input("Digite 1-Adição, 2-Subtração, 3-Multiplicação, 4-Divisão: ")
    if not operacao.isdigit():
        continue
    if int(operacao) > 4 or int(operacao)<1:
        continue
    
    numero1 = float(input("Digite o 1º número: "))
    numero2 = float(input("Digite o 2º número: "))
    if operacao == "1": 
        resultado = numero1+numero2
    elif operacao == "2": 
        resultado = numero1-numero2
    elif operacao == "3": 
        resultado = numero1*numero2
    else:
        resultado = numero1/numero2
    print("o resultado é ", resultado)
    rodar = input("Deseja calcular mais uma vez? <S/N>: ")
    contador = 0
    while rodar.upper() != "S" and rodar.upper() != "N":
        rodar = input("Opção inválida. Digite S ou N: ")
        contador = contador+1
        if contador == 3:
            print("Você excedeu o limite de tentativas.")
            rodar = "N"

