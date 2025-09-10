numeros = []

for i in range(0, 9):
    n = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(n)

soma = numeros[0]+numeros[4]+numeros[8]

print(f"A soma dos números: {numeros[0], numeros[4], numeros[8]}, é: {soma}")