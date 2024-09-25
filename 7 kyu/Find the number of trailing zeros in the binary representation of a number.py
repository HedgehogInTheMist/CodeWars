```
Given a number n, find the number of trailing zeros in its binary representation.

Examples:
4  ->  2, because 4 is represented as 100
5  ->  0, because 5 is represented as 101

Limits:
0 < n <= 10^4
```
# return the count of trailing number of zeros in a binary form of a number.
def trailing_zeros(n) ->int:
    binary = bin(n)[2:]
    return len(binary) - len(binary.rstrip('0'))