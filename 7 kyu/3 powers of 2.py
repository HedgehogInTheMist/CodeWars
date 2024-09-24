```
Write a function that accepts a number, and checks it can be represented as a sum of exactly 3 powers of 2. (n == 2**i + 2**j + 2**k, i, j, k >= 0)

For example:

three_powers(2)  # False
three_powers(3)  # True, 3 = 2**0 + 2**0 + 2**0
three_powers(5)  # True, 5 = 2**0 + 2**1 + 2**1
three_powers(15)  # False
Input
1 <= n <= 2 ** 512 - 1
There are 100 performance tests in languages with arbitrary precision integers, and a huge amount in C/Lua.

Note to translators: this kata should NOT be translated into any languages without arbitrary precision integers, as the performance requirements are not guaranteed to be properly enforceable.
```

three_powers = lambda n: n > 2 and n.bit_count() <= 3
