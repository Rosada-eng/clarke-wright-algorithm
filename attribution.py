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
    