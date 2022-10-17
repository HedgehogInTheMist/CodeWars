def digitize(n):
    # print([int(x) for x in str(n)[::-1]])
    # return [int(x) for x in (str(n)[::-1])]
    print(map(int, str(n)[::-1]))
    return map(int, str(n)[::-1])

if __name__ == '__main__':
    assert(digitize(35231) == [1,3,2,5,3])
    assert(digitize(0) == [0])
    assert(digitize(23582357) == [7,5,3,2,8,5,3,2])