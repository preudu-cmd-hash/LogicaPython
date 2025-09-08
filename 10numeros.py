numeros = []

for i in range(1, 11): # repete 10 vezes essa parte
    numero = int(input(f"Digite o {i}º número: "))
    numeros.append(numero)

pesquisa = int(input(f"Digite qual número quer encontrar e quantas vezes ele aparece na lista: "))

quantidade = numeros.count(pesquisa) # conta quantas vezes esse número aparece

posicao = [i for i, valor in enumerate(numeros) if valor == pesquisa]

if pesquisa in numeros: # renderização condicional para saber se o número está ou não na lista
    print(f"A lista é {numeros}\nO número {pesquisa} aparece {quantidade} vezes.\nAlém de apareceer nas posições: {posicao}")
else:
    print(f"O número {pesquisa} não está na lista")