```
Given a number as a parameter (between 2 and 30), return an array containing strings which form a box.
Like this:

n = 5

[
  '-----',
  '-   -',
  '-   -',
  '-   -',
  '-----'
]
n = 3

[
  '---',
  '- -',
  '---'
]
```

def box(n: int) -> str:
    line = '-'+ (n-2)*' '+ '-'
    result = [n * '-']
    for i in range(n - 2):
        result.append(line)
    result.append(n * '-')
    return result
    