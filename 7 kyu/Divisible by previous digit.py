```
Take a number and check each digit if it is divisible by the digit on its left checked and return an array of booleans.

The booleans should always start with false becase there is no digit before the first one.

Examples
73312        => [false, false, true, false, true]
2026         => [false, true, false, true]
635          => [false, false, false]
*** Remember 0 is evenly divisible by all integers but not the other way around ***
```

def divisible_by_last(number: int) -> bool:
    digits = [int(d) for d in str(number) if d.isdigit()]
    return [False] + [digits[i] % digits[i-1] == 0 if digits[i-1] != 0 else False for i in range(1, len(digits))]
    