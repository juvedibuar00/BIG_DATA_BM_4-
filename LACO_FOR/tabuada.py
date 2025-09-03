# Criar um programa que imprime a tabuada de um número inserido pelo usuário.
numero = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

