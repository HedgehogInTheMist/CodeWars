def find_needle(haystack):
    # print(f'found the needle at position {str(haystack.index("needle"))}')
    return f'found the needle at position {str(haystack.index("needle"))}'


if __name__ == '__main__':
    assert (find_needle(
        ['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]) == 'found the needle at position 3')
    assert (find_needle(['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay', 'needle',
                         'something somebody lost a while ago']) == 'found the needle at position 5')
    assert (find_needle(
        [1, 2, 3, 4, 5, 6, 7, 8, 8, 7, 5, 4, 3, 4, 5, 6, 67, 5, 5, 3, 3, 4, 2, 34, 234, 23, 4, 234, 324, 324, 'needle',
         1, 2, 3, 4, 5, 5, 6, 5, 4, 32, 3, 45, 54]) == 'found the needle at position 30')
    assert (find_needle(
        [94, 203, 140, 60, 134, 162, 126, 83, 67, 183, 198, 185, 78, 134, 187, 124, 131, 74, 184, 92, 33, 180, 229, 185,
         169, 73, 206, 76, 56, 161, 123, 59, 158, 185, 5, 180, 161, 87, 5, 137, 88, 192, 168, 82, 300, 244, 86, 89, 193,
         138, 261, 246, 105, 14, 295, 184, 106, 1, 146, 32, 269, 67, 282, 68, 2, 118, 238, 193, 7, 80, 159, 211, 69, 86,
         'needle', 187, 154, 141, 99, 226, 11, 92, 289, 229, 129, 67, 59, 105, 38, 177, 94, 227, 13, 56, 256, 258, 210,
         22, 170, 245]) == 'found the needle at position 74')

'''
Can you find the needle in the haystack?
Write a function findNeedle() that takes an array full of junk but containing one "needle"
After your function finds the needle it should return a message (as a string) that says:
"found the needle at position " plus the index it found the needle, so:

Example(Input --> Output)
["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 

'''
