from nodes import distances, cities

class Node:
    def __init__(self, id:int, city:str, demand:int=0):
        self.id = id
        self.city = city
        self.demand = demand
        self.on_route = False

    def __str__(self):
        return f"{self.id} - {self.city} ({self.demand})"
    
    def __repr__(self):
        return self.__str__()

class Route:
    def __init__(self, id:int, capacity:int = 50):
        self.id = id
        self.nodes: list[Node] = [] 
        self.distance: int = 0
        self.load: int = 0
        self.capacity: int = capacity

    def __str__(self):
        return f"Route: Load: {self.load:4.0f} \t Distance: {self.distance:6.0f} \t" + f"[{' -> '.join([str(node.id) for node in self.nodes])}]"

    def __repr__(self):
        return self.__str__()
    

    def last_node(self):
        return self.nodes[-2]
    
    def first_node(self):
        return self.nodes[1]
    
    def calc_distance(self):
        return sum(
            [
                distances[self.nodes[i].id][self.nodes[i+1].id]
                for i in range(len(self.nodes) - 1)
            ]
        )

    def calc_load(self):
        load = sum([node.demand for node in self.nodes])
        
        if load > self.capacity:
            raise ValueError(f"Route load ({load}) exceeds vehicle capacity ({self.capacity})")
        
        return load

    def __add_last_node(self, node:Node):
        self.nodes.append(node)
    
    def __add_first_node(self, node:Node):
        self.nodes.insert(0, node)
    
    def add_node(self, node:Node, beginning:bool = False):
        if beginning:
            self.__add_first_node(node)
        else:
            self.__add_last_node(node)

        self.distance = self.calc_distance()
        self.load = self.calc_load()

    def unify_route(self, route, beginning:bool = False):
        if beginning:
            nodes = route.nodes[::-1]

        else:
            nodes = route.nodes

        for node in nodes:
            self.add_node(node, beginning)

def __is_on_another_route(node:Node, routes:list[Route]):
    for route in routes:
        if node in route.nodes[1:-1]:
            return True
    return False

def __is_on_edge(node:Node, route:Route):
    return route.last_node() == node or route.first_node() == node

def clark_wright(routes:list[Route]):
    """
    Clark & Wright savings algorithm for VRP

        s_ij = c_0i + c_0j - c_ij
    """

    savings = []

    for i in range(len(routes)):
        for j in range(i+1, len(routes)):
            c_0i = distances[0][routes[i].first_node().id]
            c_0j = distances[0][routes[j].first_node().id]
            c_ij = distances[routes[i].last_node().id][routes[j].first_node().id]

            s_ij = c_0i + c_0j - c_ij

            savings.append((i, j, s_ij))

    savings.sort(key=lambda x: x[2], reverse=True)

    for i, j, saving in savings:
        route_i = routes[i]
        route_j = routes[j]

        if route_i.load + route_j.load > route_i.capacity:
            print(f"Routes {i} and {j} exceed vehicle capacity")
            continue

        i_is_on_edge = __is_on_edge(route_i.last_node(), route_i)
        j_is_on_edge = __is_on_edge(route_j.first_node(), route_j)





        route_i.unify_route(route_j)
        routes.pop(j)

    return routes


def build_initial_routes(deposit:Node, nodes:list[Node], capacity:int):   
    """"
    Builds the initial routes for the MDVRP:
        - Each node is assigned to a route attended by a single vehicle
        - The vehicle starts and ends its route at the deposit
    """

    routes = []

    deposit = nodes[0]
    for idx, node in enumerate(nodes[1:]):
        route = Route(id=idx, capacity=capacity)

        route.add_node(deposit, beginning=True)
        route.add_node(node)
        route.add_node(deposit)

        routes.append(route)

    return routes


if __name__ == "__main__":
    nodes = [Node(i, city, demand=10) for i, city in enumerate(cities, 0)]

    print(nodes)
    
    initial_routes = build_initial_routes(nodes[0], nodes, 100)

    for route in initial_routes:
        print(route)
