array = []

for i in range(1, 7):
    caracter = str(input(f"digite o {i}º caracter (letra): "))
    array.append(caracter)

invertido = list(reversed(array)) # inverte o array

"""
outras formas de inverter o array:
array.reverse()
invertido = array[::-1]
"""

print(f"A ordem normal dos caracteres é: {array}\nJá a invertida é: {invertido}")