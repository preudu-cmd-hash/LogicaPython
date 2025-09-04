def main():
    numeros = []
    
    for i in range(1, 8):
        numero = float(input(f"Digite o {i}º número: "))
        numeros.append(numero)

    maior = max(numeros) #encontra no maior número do array

    posicao = numeros.index(maior) # encontra a posição do maior número dentro do array

    print(f"O maior número entre {numeros} é: {maior}, e está na posição {posicao}")

main()