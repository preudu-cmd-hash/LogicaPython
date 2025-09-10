tabela = []

for i in range(1, 17):
    num = int(input(f"Digite o {i}º número: "))
    tabela.append(num)

for i in range(0, len(tabela), 4):
    linha = tabela[i:i+4]
    print(" ".join(f"{n:^5}" for n in linha))