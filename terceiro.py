#idade = int(input("Qual a sua idade? "))
#print(idade, "anos")
#for contador in range(idade+1):
#    print("você ja viveu por", contador, "anos")


#while 1==1:
 #   nome = input ("Digite um nome: ")
  #  if nome == "":
   #     break
    #for letra in nome:
     #   print(letra)
   # print("****************")

sair = "N"
while sair != "S":
    nome = input ("Digite um nome: ")
    for letra in nome:
        print(letra)
    print("****************")
    sair = input ("Sair do programa (S/N)?: ")