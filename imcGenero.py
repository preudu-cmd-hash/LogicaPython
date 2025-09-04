def inicio(): # Função principal, onde chama as outras funções
    nome = str(input("Digite seu nome: "))
    genero_informado = str(input("Qual seu gênero? (M ou F)"))
    peso = float(input("Quanto você pesa? (55.5)"))
    altura = float(input("Qual sua altura? (1.55)"))
    imcValor = imc(peso, altura) # Envia os parâmetros para o cálculo do IMC
    print(f"Olá {nome} o seu imc é {imcValor: .2f}! Está classificado como {classificacao_genero(genero_informado, imcValor)}") # Envia os parâmetros para a diferenciação por gênero e imprime o resultado do IMC e da classificação 

def imc(peso:float, altura:float): # Função que calcula o IMC
    return peso / (altura*altura)

def classificacao_genero(genero:str, imc:float): # Função que faz a diferenciação do IMC por gênero
    match genero.upper():
        case "M":
            if imc < 20:
                return "Abaixo do peso"
            elif imc < 25:
                return "Peso normal"
            elif imc < 30:
                return "Sobrepeso"
            else:
                return "Obesidade"
        case "F":
            if imc < 19:
                return "Abaixo do peso"
            elif imc < 24:
                return "Peso normal"
            elif imc < 29:
                return "Sobrepeso"
            else:
                return "Obesidade"
        case _:
            return "Gênero não reconhecido"

inicio()
