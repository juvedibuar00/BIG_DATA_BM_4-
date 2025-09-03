# O que é loopa while?
# É uma estrutura de controle que permite repetir um bloco de código enquanto uma condição específica for verdadeira.
# Sintaxe básica:
# while condição:
#     bloco de código a ser executado enquanto a condição for verdadeira
# Exemplo prático:
contador = 0
while contador < 200:
    print(f"Contador: {contador}")
    contador += 1  # Incrementa o contador para evitar loop infinito
    
print("Loop encerrado.")