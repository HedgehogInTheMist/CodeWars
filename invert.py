def invert(lst):
    return [-x for x in lst]


if __name__ == '__main__':
    assert(invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5])
    assert(invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5])
    assert(invert([]) == [])


'''
Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
You can assume that all values are integers. Do not mutate the input array/list.
'''