```
Given a number n we will define its scORe to be 0 | 1 | 2 | 3 | ... | n, where | is the bitwise OR operator.

Write a function that takes n and finds it's scORe.

n	scORe n
0	0
1	1
49	63
1000000	1048575
```


def score(n: int) -> int:
    power = 1
    while power <= n:
        power <<= 1
    return power - 1