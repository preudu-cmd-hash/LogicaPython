"""Escreva um programa que declare uma matriz 3x3 de números reais. O usuário deve preencher todos os elementos da matriz, e o
programa deve calcular e exibir a soma dos elementos da diagonal principal."""

numeros = []

for i in range(0, 9):
    n = float(input(f"Digite o {i + 1}º número: "))
    numeros.append(n)

soma = numeros[0]+numeros[4]+numeros[8]

print(f"A soma dos números: {numeros[0], numeros[4], numeros[8]}, é: {soma}")