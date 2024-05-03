def each_cons(lst: list, n: int) -> list:
    print(lst, n)
    print([lst[i: i + n] for i in range(len(lst) + 1 - n)])
    return [lst[i: i + n] for i in range(len(lst)+1 - n)]


each_cons([9, 9, 14, 18, 5, 14, 7, 15], 9)