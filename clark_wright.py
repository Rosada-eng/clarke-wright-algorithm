class ClarkWright:
    DEPOSIT_CAPACITY = 20

    @staticmethod
    def calculate_savings(distances):
        savings = []
        for i in range(1, len(distances)):
            for j in range(i + 1, len(distances)):
                c_0i = distances[0][i]
                c_j0 = distances[j][0]
                c_ij = distances[i][j]

                s_ij = c_0i + c_j0 - c_ij

                savings.append((i, j, s_ij))

        savings.sort(key=lambda x: x[2], reverse=True)

        return savings
    
    @staticmethod
    def is_on_any_route(node_idx, routes):
        for route in routes:
            if node_idx in route:
                return True, route
        return False, None
    
    @staticmethod
    def is_on_left_edge(node_idx, route):
        return route[1] == node_idx
    
    @staticmethod
    def is_on_right_edge(node_idx, route):
        return route[-2] == node_idx
    
    @staticmethod
    def can_store_node(node_idx, route, demands):
        return sum([demands[node] for node in route]) + demands[node_idx] <= ClarkWright.DEPOSIT_CAPACITY
    
    @staticmethod
    def can_store_routes(route_i, route_j, demands):
        return sum([demands[node] for node in route_i] + [demands[node] for node in route_j]) <= ClarkWright.DEPOSIT_CAPACITY

    @staticmethod
    def calc_routes(distances, demands):
        savings = ClarkWright.calculate_savings(distances)
        routes = []
        for i, j, s_ij in savings:
            node_i = i
            node_j = j

            node_i_on_route, route_i = ClarkWright.is_on_any_route(node_i, routes)
            node_j_on_route, route_j = ClarkWright.is_on_any_route(node_j, routes)

            if not node_i_on_route and not node_j_on_route:
                route = [0, node_j, node_i, 0]

                if not ClarkWright.can_store_routes(route, [0,0], demands):
                    continue

                routes.append(route)

            elif node_i_on_route and not node_j_on_route:
                if not ClarkWright.can_store_node(node_j, route_i, demands):
                    continue

                if ClarkWright.is_on_left_edge(node_i, route_i):
                    route_i.insert(1, node_j)

                elif ClarkWright.is_on_right_edge(node_i, route_i):
                    route_i.insert(-1, node_j)

                else:
                    continue

            elif not node_i_on_route and node_j_on_route:
                if not ClarkWright.can_store_node(node_i, route_j, demands):
                    continue

                if ClarkWright.is_on_left_edge(node_j, route_j):
                    route_j.insert(1, node_i)

                elif ClarkWright.is_on_right_edge(node_j, route_j):
                    route_j.insert(-1, node_i)

                else:
                    continue

            else:
                # both on routes
                if route_i == route_j:
                    # (i,j) is on the same route
                    continue

                else:
                    if not ClarkWright.can_store_routes(route_i, route_j, demands):
                        continue

                    if ClarkWright.is_on_left_edge(node_i, route_i) and ClarkWright.is_on_right_edge(node_j, route_j):
                        # i is on the left edge of route_i and j is on the right edge of route_j
                        # merge route_j into route_i
                        route_i.pop(0)
                        route_j.pop(-1)
                        route_j.extend(route_i)
                        routes.remove(route_i)

                    elif ClarkWright.is_on_right_edge(node_i, route_i) and ClarkWright.is_on_left_edge(node_j, route_j):
                        # i is on the right edge of route_i and j is on the left edge of route_j
                        # merge route_j into route_i
                        route_i.pop(-1)
                        route_j.pop(0)
                        route_i.extend(route_j)
                        routes.remove(route_j)

                    elif ClarkWright.is_on_left_edge(node_i, route_i) and ClarkWright.is_on_left_edge(node_j, route_j):
                        # i and j are on the left edge of their respective routes
                        # reverse route_j and merge it into route_i
                        route_i.pop(0)
                        route_j.pop(0)
                        route_j.reverse()
                        route_j.extend(route_i)
                        routes.remove(route_i)

                    elif ClarkWright.is_on_right_edge(node_i, route_i) and ClarkWright.is_on_right_edge(node_j, route_j):
                        # i and j are on the right edge of their respective routes
                        # reverse route_i and merge it into route_j
                        route_i.pop(-1)
                        route_j.pop(-1)
                        route_j.reverse()
                        route_j.extend(route_i)
                        routes.remove(route_i)

                    else:
                        continue

        return routes
    
    @staticmethod
    def append_non_attended_clients(routes, demands):
        in_route_nodes = set()
        for route in routes:
            in_route_nodes.update(route)

        non_attended_clients = set(range(1, len(demands))) - in_route_nodes

        new_routes = []

        for client in non_attended_clients:
            if demands[client] > ClarkWright.DEPOSIT_CAPACITY:
                continue

            new_routes.append([0, client, 0])

        routes.extend(new_routes)

        return routes

    @staticmethod
    def calc_total_cost(routes, distances):
        total_cost = 0
        for route in routes:
            for i in range(len(route) - 1):
                total_cost += distances[route[i]][route[i+1]]

        return total_cost
    
    @staticmethod
    def calc_total_load(routes, demands):
        total_load = 0
        for route in routes:
            for node in route:
                total_load += demands[node]

        return total_load
    

