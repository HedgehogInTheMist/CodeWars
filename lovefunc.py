def lovefunc(flower1, flower2):
    return (flower1 + flower2) % 2


if __name__ == '__main__':
    assert (lovefunc(1, 4) == True)
    assert (lovefunc(2, 2) == False)
    assert (lovefunc(0, 1) == True)
    assert (lovefunc(0, 0) == False)

'''
Timmy & Sarah think they are in love, but around where they live, they will only know once they pick a flower each.
If one of the flowers has an even number of petals and the other has an odd number of petals it means they are in love.
Write a function that will take the number of petals of each flower and return true if they are in love and false if they aren't.
'''
