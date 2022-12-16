def index(array, n):
    return pow(array(n), n) if n < len(array) else -1


if __name__ == '__main__':
    assert (index([1, 2, 3, 4], 2) == 9)
    # assert (index([1, 3, 10, 100], 3) == 1000000)
    # assert (index([5, 1], 0) == 1)
    # assert (index([3, 1], 1) == 1)
    # assert (index([1, 2], 2) == -1)
    # assert (index([1, 2], 3) == -1)
    # assert (index([7], 0) == 1)
    # assert (index([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 9) == 1)
    # assert (index([1, 1, 1, 1, 1, 1, 1, 1, 1, 100], 9) == 1000000000000000000)
    # assert (index([29, 82, 45, 10], 3) == 1000)
    # assert (index([6, 31], 3) == -1)
    # assert (index([75, 68, 35, 61, 9, 36, 89, 11, 30], 10) == -1)
