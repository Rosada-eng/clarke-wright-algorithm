# Distance of 14 clients allocated to depot `dp_São Carlos`:
distances = [
    [0, 273, 317, 362, 131, 690, 283, 969, 449, 288, 376, 522, 830, 820],
    [273, 0, 546, 497, 667, 471, 910, 167, 240, 610, 795, 487, 413, 556],
    [317, 546, 0, 792, 170, 836, 114, 399, 587, 520, 689, 541, 547, 764],
    [362, 497, 792, 0, 310, 751, 117, 414, 229, 981, 589, 429, 705, 861],
    [131, 667, 170, 310, 0, 373, 1000, 460, 805, 746, 470, 258, 692, 944],
    [690, 471, 836, 751, 373, 0, 682, 342, 890, 241, 384, 160, 818, 850],
    [283, 910, 114, 117, 1000, 682, 0, 100, 820, 729, 487, 563, 683, 872],
    [969, 167, 399, 414, 460, 342, 100, 0, 450, 493, 368, 424, 516, 449],
    [449, 240, 587, 229, 805, 890, 820, 450, 0, 168, 341, 123, 215, 943],
    [288, 610, 520, 981, 746, 241, 729, 493, 168, 0, 651, 115, 347, 300],
    [376, 795, 689, 589, 470, 384, 487, 368, 341, 651, 0, 664, 715, 998],
    [522, 487, 541, 429, 258, 160, 563, 424, 123, 115, 664, 0, 206, 839],
    [830, 413, 547, 705, 692, 818, 683, 516, 215, 347, 715, 206, 0, 752],
    [820, 556, 764, 861, 944, 850, 872, 449, 943, 300, 998, 839, 752, 0],
]

# Demands of allocated clients
demands = [
    0, 19, 19, 9, 8, 5, 12, 6, 15, 20, 12, 15, 19, 17, 10
]

# One of the resulted allocation from `attribution_example.py`
clients_allocated = [
    35, 41, 23, 47, 37, 24, 8, 17, 4, 46, 7, 43
]

if __name__ == "__main__":
    from clark_wright import ClarkWright

    routes = ClarkWright.calc_routes(distances, demands)
    routes = ClarkWright.append_non_attended_clients(routes, demands)

    total_cost = ClarkWright.calc_total_cost(routes, distances)
    total_load = ClarkWright.calc_total_load(routes, demands)

    print(f'Total cost: {total_cost}')
    print(f'Total load: {total_load}')
    print(f'Number of routes: {len(routes)}')
    print()
    
    for route in routes:
        print(route, f'({sum([demands[node] for node in route])})')

    """"
    Output:

    Total cost: 7092
    Total load: 357
    Number of routes: 5

    Routes:
        [0, 2, 1, 7, 6, 3, 0] (95)
        [0, 13, 9, 12, 5, 4, 0] (94)
        [0, 8, 0] (58)
        [0, 10, 0] (53)
        [0, 11, 0] (57)
        
    """