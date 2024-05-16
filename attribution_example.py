# distance of clients to deposits
clients_to_deposit = [
    [311, 462, 371, 182],
    [172, 136, 428, 162],
    [283, 379, 380, 190],
    [289, 80, 63, 136],
    [385, 481, 274, 384],
    [83, 292, 265, 214],
    [135, 401, 123, 346],
    [167, 362, 295, 73],
    [394, 349, 290, 450],
    [461, 187, 445, 50],
]

# demands of clients
demands = [
    12, 10, 8, 6, 4, 2, 14, 16, 18, 20
]

# capacities of deposits
depot_capcities = [
    30, 42, 36, 38
]

depot_names = [
    "dp_Recife",
    "dp_Imperatriz",
    "dp_Limeira",
    "dp_São Carlos"
]

if __name__ == "__main__":
    from parallel_attribution import ParallelAttribution

    clients_in_deposits = ParallelAttribution.attribuite(clients_to_deposit, demands, depot_capcities)

    for deposit, clients in enumerate(clients_in_deposits):
        total_demand = sum([demands[client] for client in clients])
        print(f'Deposit {depot_names[deposit]}: \t clients: {clients} \t demand: {total_demand} / {depot_capcities[deposit]}')