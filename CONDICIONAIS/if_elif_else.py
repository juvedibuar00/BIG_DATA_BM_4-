# O que é condcional multipla if, elif e else?
# É uma estrutura de controle que permite testar múltiplas condições em sequência, executando o bloco de código correspondente à primeira condição verdadeira.
# Sintaxe básica:
# if condição1:
#     bloco de código a ser executado se a condição1 for verdadeira
# elif condição2:
#     bloco de código a ser executado se a condição2 for verdadeira
# elif condição3:
#     bloco de código a ser executado se a condição3 for verdadeira
# ...
# else:
#     bloco de código a ser executado se nenhuma das condições anteriores for verdadeira
# Exemplo prático:
idade = int(input("Digite sua idade: "))
if idade < 0:
    print("Idade inválida.")
elif idade < 18:
    print("Você é menor de idade.")
    print(f"Não pode votar nem dirigir com {idade} anos.")
elif idade < 65:
    print("Você é adulto.")
    print(f"Pode votar e dirigir com {idade} anos.")
else:
    print("Você é idoso.")
    print(f"Pode votar e dirigir com {idade} anos, e tem direito a benefícios especiais.")
