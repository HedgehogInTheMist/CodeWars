```
Return the nth term of the Recamán's sequence.

a(0) = 0;

        a(n-1) - n, if this value is positive and not yet in the sequence
      /
a(n) <
      \
        a(n-1) + n, otherwise
input range: 0 – 30 000

Numberphile video about Recamán's sequence
```

def recaman(n: int):
    if n == 0:
        return 0
    
    sequence = [0] * (n + 1)
    seen = set()
    seen.add(0)
    
    for i in range(1, n + 1):
        prev = sequence[i - 1]
        candidate = prev - i
        
        if candidate > 0 and candidate not in seen:
            sequence[i] = candidate
        else:
            sequence[i] = prev + i
        
        seen.add(sequence[i])
    
    return sequence[n]