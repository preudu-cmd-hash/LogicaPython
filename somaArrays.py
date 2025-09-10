numbers1 = []
numbers2 = []

for i in range(1, 5):
    n1 = int(input(f"Digite o {i}º número do primeiro array: "))
    numbers1.append(n1)
    n2 = int(input(f"Digite o {i}º número do segundo array: "))
    numbers2.append(n2)

sumArrays = [numbers1[i] + numbers2[i] for i in range(4)]

print(sumArrays)