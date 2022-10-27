def two_sort(array):
    return '***'.join(min(array))


if __name__ == '__main__':
    assert(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]) == 'b***i***t***c***o***i***n' )
    assert(two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]) == 'a***r***e')
    assert(two_sort(["lets", "talk", "about", "javascript", "the", "best", "language"]) == 'a***b***o***u***t')
    assert(two_sort(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]) == 'c***o***d***e')
    assert(two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]) == 'L***e***t***s')

'''
You will be given a list of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.
The returned value must be a string, and have "***" between each of its letters.
You should not remove or add elements from/to the array.
'''