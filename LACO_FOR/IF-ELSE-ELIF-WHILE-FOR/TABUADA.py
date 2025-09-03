# FAÇA UM PROGRAMA  - CALCULADORA
# 4 OPERAÇÕES BÁSICA - SOMA - SUB - DIVISÃO - MULTIPLICAÇÃO
# RECEBER DOIS NÚMEROS
# REVISÃO DO IF ELIF ELSE

print("------- NÚMEROS -------")
numeroUm = int(input("Digite o 1º número: "))
numeroDois = int(input("Digite o 2º número: "))
print("-----------------------\n")

print("------- OPERAÇÕES  -------")
print("1 - SOMA\n"
      "2 - SUBTRAIR\n"
      "3 - MULTIPLICAÇÃO\n"
      "4 - DIVISÃO\n")
operacao = input("Escolha uma operação: ")
print("---- \n")
if operacao == "1" or operacao == "SOMA" or operacao == "+":
    print(f"Resultado da soma: {numeroUm + numeroDois}")
elif operacao == "2":
    print(f"Resultado da subtração: {numeroUm - numeroDois}")
elif operacao == "3":
    print(f"Resultado da multiplicação: {numeroUm * numeroDois}")
elif operacao == "4":
    print(f"Resultado da divisão: {numeroUm / numeroDois}")
else:
    print(f"Operação invalida!")

print("-----------------------\n")





CALCULADORA WHILE


# FAÇA UM PROGRAMA  - CALCULADORA
# 4 OPERAÇÕES BÁSICA - SOMA - SUB - DIVISÃO - MULTIPLICAÇÃO
# RECEBER DOIS NÚMEROS
# REVISÃO DO IF ELIF ELSE

while True:
    print("------- OPERAÇÕES  -------")
    print("1 - SOMA\n"
          "2 - SUBTRAIR\n"
          "3 - MULTIPLICAÇÃO\n"
          "4 - DIVISÃO\n"
          "5 - SAIR")
    operacao = input("Escolha uma operação: ")
    if operacao == "5" or operacao == "SAIR":
        print(f"Até logo....")
        break

    print("------- NÚMEROS -------")
    numeroUm = int(input("Digite o 1º número: "))
    numeroDois = int(input("Digite o 2º número: "))
    print("-----------------------\n")


    print("---- \n")
    if operacao == "1" or operacao == "SOMA" or operacao == "+":
        print(f"Resultado da soma: {numeroUm + numeroDois}")
    elif operacao == "2":
        print(f"Resultado da subtração: {numeroUm - numeroDois}")
    elif operacao == "3":
        print(f"Resultado da multiplicação: {numeroUm * numeroDois}")
    elif operacao == "4":
        print(f"Resultado da divisão: {numeroUm / numeroDois}")
    else:
        print(f"Operação invalida!")

    print("-----------------------\n")
    print("\n")