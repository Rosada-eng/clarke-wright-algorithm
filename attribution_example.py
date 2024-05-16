import random 

# distance of clients to deposits
clients_to_deposit = [
    [489, 50, 466, 157],
    [212, 171, 94, 179],
    [160, 431, 85, 95],
    [59, 487, 284, 99],
    [499, 254, 234, 67],
    [68, 490, 498, 85],
    [485, 269, 149, 417],
    [396, 396, 78, 412],
    [435, 138, 284, 68],
    [256, 103, 192, 289],
    [446, 295, 309, 486],
    [450, 111, 172, 329],
    [122, 123, 445, 339],
    [198, 115, 246, 422],
    [185, 204, 372, 275],
    [312, 385, 233, 481],
    [423, 417, 74, 305],
    [366, 248, 361, 95],
    [407, 170, 396, 319],
    [160, 141, 335, 312],
    [288, 92, 204, 216],
    [215, 426, 411, 335],
    [207, 72, 322, 205],
    [175, 309, 352, 141],
    [210, 473, 394, 161],
    [405, 318, 73, 123],
    [265, 100, 111, 111],
    [70, 457, 186, 107],
    [156, 338, 199, 364],
    [387, 205, 123, 426],
    [130, 189, 291, 280],
    [50, 135, 430, 230],
    [474, 132, 155, 168],
    [139, 305, 102, 402],
    [168, 182, 459, 201],
    [366, 384, 397, 288],
    [380, 377, 177, 260],
    [303, 370, 374, 199],
    [402, 291, 370, 319],
    [467, 348, 171, 331],
    [157, 79, 397, 187],
    [440, 247, 206, 179],
    [108, 441, 88, 311],
    [452, 392, 394, 87],
    [480, 198, 135, 193],
    [406, 400, 291, 455],
    [449, 316, 450, 105],
    [396, 363, 499, 278],
    [255, 419, 288, 432],
    [52, 353, 238, 105],
]

# demands of clients
demands = [
    random.randint(5, 20) for _ in range(len(clients_to_deposit))
]

# capacities of deposits
depot_capcities = [
    120, 200, 150, 220
]

depot_names = [
    "dp_Recife",
    "dp_Imperatriz",
    "dp_Limeira",
    "dp_São Carlos"
]

print('demands:', demands)

if __name__ == "__main__":
    from parallel_attribution import ParallelAttribution

    clients_in_deposits = ParallelAttribution.attribuite(clients_to_deposit, demands, depot_capcities)

    for deposit, clients in enumerate(clients_in_deposits):
        total_demand = sum([demands[client] for client in clients])
        print(f'Deposit {depot_names[deposit]}: \t clients({len(clients)}): {clients} \t demand: {total_demand} / {depot_capcities[deposit]}')