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

demands = [
    12, 10, 8, 6, 4, 2, 14, 16, 18, 20
]

capcities = [
    30, 32, 30, 25
]

class ParallelAttribution:
    @staticmethod
    def can_store_client(deposit, capcities, client, demands, clients_in_deposits):
        stored = sum([demands[client] for client in clients_in_deposits[deposit]])
        
        return stored + demands[client] <= capcities[deposit]
    
    @staticmethod
    def calc_urgency(clients_to_deposit):
        urgencies = []

        for client in range(len(clients_to_deposit)):
            closest_distance = min(clients_to_deposit[client])

            urgency = sum(
                [
                    closest_distance - distance
                    for distance in clients_to_deposit[client]
                ]
            )

            urgencies.append((client, urgency))

        urgencies.sort(key=lambda x:x[1], reverse=True)

        return urgencies
    

    @staticmethod
    def attribuite(clients_to_deposit, demands, capacities):
        urgencies = ParallelAttribution.calc_urgency(clients_to_deposit)

        clients_in_deposits = [[] for _ in capacities]
        overload_deposits = []
        attributed_client = []

        for client, _ in urgencies:
            if client in attributed_client:
                continue

            closest_deposits = [
                (deposit, distance)
                for deposit, distance in enumerate(clients_to_deposit[client])
            ]

            closest_deposits.sort(key=lambda x:x[1])

            for deposit, _ in closest_deposits:
                if ParallelAttribution.can_store_client(deposit, capacities, client, demands, clients_in_deposits):
                    clients_in_deposits[deposit].append(client)
                    attributed_client.append(client)
                    break


        for deposit, clients in enumerate(clients_in_deposits):
            total_demand = sum([demands[client] for client in clients])
            print(f'Deposit {deposit}: [{clients}] ({total_demand})')

        ParallelAttribution.all_clients_attributed(attributed_client, clients_to_deposit)

        return clients_in_deposits

    @staticmethod
    def all_clients_attributed(attributed_clients, clients_to_deposit):
        if not len(attributed_clients) == len(clients_to_deposit):
            raise Exception('Not all clients were attributed. Check deposit capacities.')

if __name__ == "__main__":
    clients_in_deposits = ParallelAttribution.attribuite(clients_to_deposit, demands, capcities)



    