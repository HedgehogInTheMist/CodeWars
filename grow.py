import math
def grow(arr):
    result = 0
    for i in arr:
        result *= i
    return result
    # return math.prod(arr)

if __name__ == '__main__':
    assert(grow([1, 2, 3]) == 6)
    assert(grow([4, 1, 1, 1, 4]) == 16)
