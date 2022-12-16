def reverse_words(s):
    return ' '.join(s.split()[::-1])

if __name__ == '__main__':
    assert(reverse_words("hello world!") == "world! hello")
    assert(reverse_words("yoda doesn't speak like this") == "this like speak doesn't yoda")
    assert (reverse_words("foobar") == "foobar")
    assert (reverse_words("kata editor") == "editor kata")
    assert (reverse_words("row row row your boat") == "boat your row row row")
