"""Escreva um programa que declare duas matrizes de tamanho 2x2. O usuário deve preencher as duas matrizes com números inteiros, e o
programa deve criar uma terceira matriz que seja a soma das duas primeiras, elemento por elemento, exibindo o resultado ao final."""

numbers1 = []
numbers2 = []

for i in range(1, 5):
    n1 = int(input(f"Digite o {i}º número do primeiro array: "))
    numbers1.append(n1)
    n2 = int(input(f"Digite o {i}º número do segundo array: "))
    numbers2.append(n2)

sumArrays = [numbers1[i] + numbers2[i] for i in range(4)]

print(sumArrays)