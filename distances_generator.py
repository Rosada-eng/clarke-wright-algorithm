import random

N_CITIES = 14
N_DEPOSITS = 4

def distances_to_single_deposit(n_clients):
    distances = [[0 for i in range(n_clients)] for j in range(n_clients)]

    for i in range(n_clients):
        for j in range(i, n_clients):
            d = random.randint(100, 1000)
            if j == i:
                continue
            else:
                distances[i][j] = d
                distances[j][i] = d

    return distances

def distances_to_multiple_deposits(n_clients, n_deposits):
    distances = [
        [
            random.randint(50, 500) 
            for i in range(n_deposits)
        ] for j in range(n_clients)
    ]

    return distances

if __name__ == "__main__":

    distances = distances_to_single_deposit(N_CITIES)
    
    print('Distances to one deposit (routing):')
    for row in distances:
        print(row)
    
    distances = distances_to_multiple_deposits(N_CITIES, N_DEPOSITS)

    print('Distances to multiple deposits (attribution):')
    
    for row in distances:
        print(row)

