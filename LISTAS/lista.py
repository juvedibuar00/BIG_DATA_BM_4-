# O qué uma lista?
# É uma estrutura de dados que armazena uma coleção ordenada de itens, que podem ser de tipos diferentes.
# Sintaxe básica:
# minha_lista = [item1, item2, item3, ...]
# Exemplo prático:
minha_lista = [10, "Olá", 3.14, True]
print("Minha lista:", minha_lista)

# Acessando elementos da lista
print("Primeiro elemento:", minha_lista[0])  # Acessa o primeiro elemento

# Acessando o último elemento
print("Último elemento:", minha_lista[-1])  # Acessa o último elemento

# Modificando um elemento da lista
minha_lista[1] = "Mundo"
print("Lista após modificação:", minha_lista)

# Adicionando um elemento ao final da lista
minha_lista.append("Novo item")
print("Lista após adicionar um item:", minha_lista)

# Removendo um elemento da lista
minha_lista.remove(3.14)
print("Lista após remover um item:", minha_lista)

# Iterando sobre os elementos da lista
print("Iterando sobre a lista:")
for item in minha_lista:
    print(item)

# Verificando o tamanho da lista
print("Tamanho da lista:", len(minha_lista))

# Verificando se um item está na lista
print("3.14 está na lista?", 3.14 in minha_lista)
print("Mundo está na lista?", "Mundo" in minha_lista)

# Limpando a lista
minha_lista.clear()
print("Lista após limpar:", minha_lista)

# Lista aninhada (lista dentro de outra lista)
lista_aninhada = [1, 2, [3, 4], 5]
print("Lista aninhada:", lista_aninhada)

# Acessando elementos da lista aninhada

print("Elemento aninhado:", lista_aninhada[2][0])  # Acessa o primeiro elemento da lista aninhada

print("Elemento aninhado:", lista_aninhada[2][1])  # Acessa o segundo elemento da lista aninhada

print("Elemento aninhado:", lista_aninhada[3])     # Acessa o quarto elemento da lista principal

print("Elemento aninhado:", lista_aninhada[0])     # Acessa o primeiro elemento da lista principal

print("Elemento aninhado:", lista_aninhada[1])     # Acessa o segundo elemento da lista principal

print("Elemento aninhado:", lista_aninhada[2])     # Acessa a lista aninhada completa

print("Elemento aninhado:", lista_aninhada[2][0])  # Acessa o primeiro elemento da lista aninhada

print("Elemento aninhado:", lista_aninhada[2][1])  # Acessa o segundo elemento da lista aninhada

# Qual é extensao para anaconda
# .conda
# .yml
# .yaml
# .txt
# .env
# .json
# .ini
# .cfg
# .xml
# .csv
# .py
# .ipynb
# .r