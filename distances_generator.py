import random

destinies = [
    "Depósito",
    "São Carlos",
    "Araraquara",
    "Ribeirão Preto",
    "São Paulo",
    "Campinas",
    "Sorocaba",
    "Bauru",
    "Presidente Prudente",
    "São José do Rio Preto",
    "Limeira",
]

distances = [[0 for i in range(len(destinies))] for j in range(len(destinies))]

for i in range(len(destinies)):
    for j in range(i, len(destinies)):
        d = random.randint(100, 1000)
        if j == i:
            continue
        else:
           distances[i][j] = d
           distances[j][i] = d

for row in distances:
    print(row)