def check(seq, elem):
    return elem in seq


if __name__ == '__main__':
    assert(check([66, 101], 66) == True)
    assert(check([78, 117, 110, 99, 104, 117, 107, 115], 8) == False)
    assert(check([101, 45, 75, 105, 99, 107], 107) == True)
    assert(check([80, 117, 115, 104, 45, 85, 112, 115], 45) == True)

'''
You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
Array can contain numbers or strings. X can be either.
Return true if the array contains the value, false if not.
'''