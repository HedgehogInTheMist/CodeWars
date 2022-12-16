def array_madness(a, b):
    return sum(map(lambda x: x ** 2, a)) > sum(map(lambda x: x ** 3, b))


if __name__ == '__main__':
    assert(array_madness([4, 5, 6], [1, 2, 3]) == True)
    assert(array_madness([1, 2, 3],[4, 5, 6]) == False)
    assert(array_madness([875, 575, 413], [17, 23]) == True)
    assert(array_madness([468, 194, 566, 899, 1054, 962, 457, 399, 180], [10, 18, 26, 7, 3, 29, 19, 17, 6, 16]) == True)


'''
SpeedCode #2 - Array Madness
Objective
Given two integer arrays a, b, both of length >= 1, create a program that returns true if the sum of the squares of each element in a is strictly greater than the sum of the cubes of each element in b.
E.g.
array_madness([4, 5, 6], [1, 2, 3]) => True #because 4 ** 2 + 5 ** 2 + 6 ** 2 > 1 ** 3 + 2 ** 3 + 3 ** 3
'''