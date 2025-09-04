def main(): #Função para definir os números que estarão no array
    numeros = []
    for i in range(1, 6):
        numero = int(input(f"Digite o {i}º número: "))
        numeros.append(numero)
    print(f"A soma dos números {numeros} é: {soma(numeros)}")

def soma(numeros:int): #função para somar os números do array
    return sum(numeros)

main()