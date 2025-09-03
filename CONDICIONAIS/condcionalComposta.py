# O que é condicional composta if e else?
# É uma estrutura de controle que permite executar um bloco de código se uma condição for verdadeira e outro bloco se a condição for falsa.
# Sintaxe básica:
# if condição:
#     bloco de código a ser executado se a condição for verdadeira
# else:
#     bloco de código a ser executado se a condição for falsa
# Exemplo prático:
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Você é maior de idade.")
    print(f"Pode votar e dirigir com {idade} anos.")
else:
    print("Você é menor de idade.")
    print(f"Não pode votar nem dirigir com {idade} anos.")
