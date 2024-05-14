import random

N_CITIES = 10
N_DEPOSITS = 4

def distances_to_single_deposit():
    distances = [[0 for i in range(N_CITIES)] for j in range(N_CITIES)]

    for i in range(N_CITIES):
        for j in range(i, N_CITIES):
            d = random.randint(100, 1000)
            if j == i:
                continue
            else:
                distances[i][j] = d
                distances[j][i] = d

    for row in distances:
        print(row)

    return distances

def distances_to_multiple_deposits():
    distances = [
        [
            random.randint(50, 500) 
            for i in range(N_DEPOSITS)
        ] for j in range(N_CITIES)
    ]

    print(distances)

    return distances

if __name__ == "__main__":

    distances_to_multiple_deposits()
    distances_to_single_deposit()