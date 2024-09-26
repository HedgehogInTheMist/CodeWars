```
Given the size n of an identity matrix (I), find the number represented by the identity matrix values as its bits.

Examples:
Identity matrix of size 4:
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
should return 33825

Explanation: 1000_0100_0010_0001 -> 33825

Identity matrix of size 2:
1 0
0 1
should return 9

Explanation: 10_01 -> 1x(2^0) + 1x(2^3) = 9

Limits:
0 < n < 65
length code <= 1024
```

def soln(n):
    return int(('0'*n).join('1'*n), 2)