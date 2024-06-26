def remove(s):
    return s[:-1] if s != '' and s[-1] == '!' else s

if __name__ == '__main__':
    assert(remove("Hi!") == "Hi")
    assert(remove("Hi!!!") == "Hi!!")
    assert(remove("!Hi") == "!Hi")
    assert(remove("!Hi!") == "!Hi")
    assert(remove("Hi! Hi!") == "Hi! Hi")
    assert(remove("Hi") == "Hi")
    assert(remove("") == "")

'''
Remove an exclamation mark from the end of a string. For a beginner kata, you can assume that the input data is always a string, no need to verify it.
Examples
remove("Hi!") == "Hi"
remove("Hi!!!") == "Hi!!"
remove("!Hi") == "!Hi"
remove("!Hi!") == "!Hi"
remove("Hi! Hi!") == "Hi! Hi"
remove("Hi") == "Hi"
'''