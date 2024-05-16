from distances_generator import distances_to_single_deposit, distances_to_multiple_deposits
import random 

N_CLIENTS = 50
N_DEPOSITS = 4

clients_to_deposits_distances = distances_to_multiple_deposits(N_CLIENTS, N_DEPOSITS)

clients_demands = [random.randint(5, 20) for _ in range(N_CLIENTS)]

depot_capcities = [120, 200, 150, 220]

if __name__ == "__main__":
    from parallel_attribution import ParallelAttribution
    from clark_wright import ClarkWright

    clients_in_deposits = ParallelAttribution.attribuite(clients_to_deposits_distances, clients_demands, depot_capcities)

    print('\nAll clients attributed.\n')

    for deposit, clients in enumerate(clients_in_deposits):
        total_demand = sum([clients_demands[client] for client in clients])
        print(f'Deposit {[deposit]}:\n\tclients: {len(clients):2.0f}: {clients} \n\tdemand: {total_demand} / {depot_capcities[deposit]}\n')

    print('======================'*5)

    for deposit, clients in enumerate(clients_in_deposits):
        print(f'\n|= Routes from Deposit [{deposit}]:\n')

        clients_demands_in_deposit = [clients_demands[client] for client in clients]
        distances_to_deposit = distances_to_single_deposit(len(clients_demands_in_deposit))

        routes = ClarkWright.calc_routes(distances_to_deposit, clients_demands_in_deposit)
        routes = ClarkWright.append_non_attended_clients(routes, clients_demands_in_deposit)

        total_cost = ClarkWright.calc_total_cost(routes, distances_to_deposit)
        total_load = ClarkWright.calc_total_load(routes, clients_demands_in_deposit)

        print(f' -Total cost: {total_cost}')
        print(f' -Total load: {total_load}')
        print(f' -Number of routes: {len(routes)}')
        print()
        
        for route in routes:
            print('  ',route, f'({sum([clients_demands_in_deposit[node] for node in route])})')

        print('\n', '---------------------'*5)

