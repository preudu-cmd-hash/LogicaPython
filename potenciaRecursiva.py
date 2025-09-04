def main(): # Função principal do código que chama a função de potência
    base = int(input("Digite a base: "))
    expoente = int(input("Digite o expoente: "))

    print(f"O resultado é: {pot(base, expoente)}")

def pot(base:int, expoente:int): # Função que calcula a potenciação
    if expoente == 0:
        return 1
    else:
        return base * pot(base, expoente -1)

main()
