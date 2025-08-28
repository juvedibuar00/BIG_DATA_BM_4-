# Peça dois numeros do usuario, podendo ser inteiro ou fluante. Depois, mostre:
'''
Soma
Divisao
Subratracao
Multiplicacao
Resto da divisao?

'''

primeiroNumero = int(input("Digite o 1º numero: "))
segudnoNumero = int(input("Digite o 2º numero: "))

operacoesSugeridas = (f"A soma é igual a {primeiroNumero + segudnoNumero}, a divisão é igual {primeiroNumero/segudnoNumero}, a subtracao é igual a {primeiroNumero-segudnoNumero}, a multiplicacao é igual a {segudnoNumero * primeiroNumero} e o resto da didivisao é {primeiroNumero % segudnoNumero}")
print(operacoesSugeridas)

