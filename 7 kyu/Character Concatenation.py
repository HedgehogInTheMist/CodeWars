```
Given a string, you progressively need to concatenate the first character from the left and the first character
from the right and "1", then the second character from the left and the second character from the right and "2",
and so on.
If the string's length is odd drop the central element.
For example:
char_concat("abcdef")    == 'af1be2cd3'
char_concat("abc!def")   == 'af1be2cd3' # same result
```
def char_concat(word):
    length = len(word)
    sr = [''.join(i) for i in list(zip(word[:length//2], word[length//2:][::-1]))]
    return ''.join([(v + str(i)) for i, v in enumerate(sr, start=1)])   