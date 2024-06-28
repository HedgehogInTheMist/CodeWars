```
Reverse and invert all integer values in a given list.

reverse_invert([1,12,'a',3.4,87,99.9,-42,50,5.6]) = [-1,-21,-78,24,-5]
Remove all types other than integer.
```

def reverse_invert(lst: list) -> list:
    ints_only = [i for i in lst if isinstance(i, int)]
    zeroes_ones = [1 if i > 0 else 0 for i in ints_only]
    reversed_ints = [int(str(abs(i))[::-1]) for i in ints_only]
    return list(-abs(i) if j == 1 else i for i, j in zip(reversed_ints, zeroes_ones))