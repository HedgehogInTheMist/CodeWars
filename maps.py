def maps(a):
    print([x * 2 for x in a])
    # return list(map(lambda x:2*x, a))
    return [x * 2 for x in a]


if __name__ == '__main__':
    assert (maps([]) == [])
    assert (maps([1, 2, 3]) == [2, 4, 6])
    assert (maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18])

'''
Given an array of integers, return a new array with each value doubled.

For example:
[1, 2, 3] --> [2, 4, 6]
'''
