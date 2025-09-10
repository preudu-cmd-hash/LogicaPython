"""Escreva um programa que declare uma matriz 5x5 de números inteiros. O usuário deve preencher a matriz, e, em seguida, informar um
número para pesquisa. O programa deve mostrar a posição (linha e coluna) onde o número foi encontrado ou exibir uma mensagem
avisando que o número não existe na matriz."""

numeros = []

for i in range(0, 25): # repete 10 vezes essa parte
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

pesquisa = int(input(f"Digite qual número quer encontrar e quantas vezes ele aparece na lista: "))

quantidade = numeros.count(pesquisa) # conta quantas vezes esse número aparece

posicao = [i for i, valor in enumerate(numeros) if valor == pesquisa]

if pesquisa in numeros: # renderização condicional para saber se o número está ou não na lista
    print(f"A lista é {numeros}\nO número {pesquisa} aparece {quantidade} vezes.\nAlém de apareceer nas posições: {posicao}")
else:
    print(f"O número {pesquisa} não está na lista")