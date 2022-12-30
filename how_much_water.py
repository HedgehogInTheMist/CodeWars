def how_much_water(water: int, load: int, clothes: int):
    result = round(water * (1.1 ** (clothes - load)), 2)
    return 'Too much clothes' if clothes / load > 2 else 'Not enough clothes' if clothes < load else result



