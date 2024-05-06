```
Task
Your task is to find the smallest number which is evenly divided by all numbers between m and n (both inclusive).

Example
For m = 1, n = 2, the output should be 2.

For m = 2, n = 3, the output should be 6.

For m = 3, n = 2, the output should be 6 too.

For m = 1, n = 10, the output should be 2520.

Input/Output
[input] integer m
1 ≤ m ≤ 25

[input] integer n
1 ≤ n ≤ 25

[output] an integer
```
def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def lcm(x, y):
        return (x * y) // gcd(x, y)

def mn_lcm(m: int, n: int) -> int:
    if m > n:
        m, n = n, m
    least_multiple = 1
    for i in range(m, n + 1):
        least_multiple = lcm(least_multiple, i)
    return least_multiple