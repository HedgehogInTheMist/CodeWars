def reverse_seq(n):
    return [x + 1 for x in reversed(range(n))]


if __name__ == '__main__':
    assert(reverse_seq(5) == [5,4,3,2,1])
    assert(reverse_seq(25) == [25,24,23,22,21,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1])