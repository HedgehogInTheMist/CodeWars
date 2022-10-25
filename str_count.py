def str_count(strng, letter):
    return strng.count(letter)

if __name__ == '__main__':
    assert(str_count('hello', 'l') == 2)
    assert(str_count('hello', 'e') == 1)
    assert(str_count('codewars', 'c') == 1)
    assert(str_count('ggggg', 'g') == 5)
    assert(str_count('hello world', 'o') == 2)
    assert(str_count('', 'z') == 0)