distances = [
    [0, 711, 461, 167, 480, 532, 984, 676, 587, 950, 599],
    [711, 0, 316, 536, 124, 143, 493, 782, 838, 758, 361],
    [461, 316, 0, 159, 915, 410, 881, 250, 845, 193, 111],
    [167, 536, 159, 0, 937, 466, 754, 110, 902, 569, 310],
    [480, 124, 915, 937, 0, 673, 157, 303, 151, 720, 439],
    [532, 143, 410, 466, 673, 0, 991, 944, 404, 156, 958],
    [984, 493, 881, 754, 157, 991, 0, 804, 430, 759, 443],
    [676, 782, 250, 110, 303, 944, 804, 0, 354, 797, 222],
    [587, 838, 845, 902, 151, 404, 430, 354, 0, 881, 310],
    [950, 758, 193, 569, 720, 156, 759, 797, 881, 0, 142],
    [599, 361, 111, 310, 439, 958, 443, 222, 310, 142, 0],
]

names = [
    "Depósito",
    "São Carlos",
    "Araraquara",
    "Ribeirão Preto",
    "São Paulo",
    "Campinas",
    "Sorocaba",
    "Bauru",
    "Presidente Prudente",
    "São José do Rio Preto",
    "Limeira",
]

demands = [
    0, 12, 10, 8, 6, 4, 2, 14, 16, 18, 20
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