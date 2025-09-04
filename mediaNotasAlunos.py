# Lista para armazenar as notas
notas = []

# Recebe as notas dos 4 alunos
for i in range(1, 5):
    nota = float(input(f"Digite a nota do {i}º aluno: "))
    notas.append(nota)

# Calcula a média da turma
media = 6
media_turma = sum(notas) / len(notas)
print(f"\nMédia da turma é: {media_turma:.2f}")

# Listas para notas acima e abaixo da média
acima_media = [nota for nota in notas if nota >= media]
abaixo_media = [nota for nota in notas if nota < media]

# Mostra os resultados
print(f"Notas acima da média: {acima_media}")
print(f"Notas abaixo da média: {abaixo_media}")
