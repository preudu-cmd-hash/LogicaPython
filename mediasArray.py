def main():
    notas = []
    for i in range(1, 5):
        nota = float(input(f"Digite a nota {i}: "))
        notas.append(nota)
    mediaNotas = media(notas)
    print(f"As notas desse aluno são: {notas}, e a média das notas desse aluno é: {mediaNotas}")
    if mediaNotas >= 6:
        print("APROVADO!")
    else:
        print("REPROVADO!")

def media(notas):
    return sum(notas) / len(notas)

main()