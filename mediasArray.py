def main(): # Função principal 
    notas = []
    
    for i in range(1, 5):
        nota = float(input(f"Digite a nota {i}: "))
        notas.append(nota)
        
    mediaNotas = media(notas) # Envia as notas para calcular a média
    
    print(f"As notas desse aluno são: {notas}, e a média das notas desse aluno é: {mediaNotas}")
    
    if mediaNotas >= 6: # Condicional de aprovação
        print("APROVADO!")
    else:
        print("REPROVADO!")

def media(notas): # Cálculo da média
    return sum(notas) / len(notas)

main()
