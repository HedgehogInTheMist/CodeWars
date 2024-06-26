```
Tranform of input array of zeros and ones to array in which counts number of continuous ones. If there is none, return an empty array

Example
[1, 1, 1, 0, 1] -> [3,1]
[1, 1, 1, 1, 1] -> [5]
[0, 0, 0, 0, 0] -> []
```

from itertools import groupby

def ones_counter(inp):
    result = []
    for key, group in groupby(inp):
        if key == 1:
            result.append(len(list(group)))
    return result