def main():
    notas = []
    for i in range(0, 4):
        nota = float(input(f"Digite a nota {i + 1}: "))
        notas.append(nota)
    mediaNotas = media(notas)
    print(f"A média das notas desse aluno é: {mediaNotas}")
    if mediaNotas > 6:
        print("APROVADO!")
    else:
        print("REPROVADO!")

def media(notas):
    return sum(notas) / len(notas)

main()