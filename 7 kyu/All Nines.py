```
Task
Given any positive integer x ≤ 4000, find the smallest positive integer m such that mx consists of all 9's. 
Return -1 if no such m exists.
Examples:
11 -> 9, because 11 * 9 == 99.
12 -> -1, because 12 is even, so no multiple of it can contain only nines.
13 -> 76923, because 13 * 76923 == 999999, and no smaller positive integer, when multiplied by 13, 
generates an integer containing only nines.
NOTE: Although x ≤ 4000, m can be very very LARGE. Where necessary, the way of handling big integers 
appropriate to the language should be used.
```

from collections import deque

def all_nines(x: int) -> int:
    queue = deque()
    queue.append('9')        
    visited = set()    
    while queue:
        current = queue.popleft()                
        current_num = int(current)
        if current_num % x == 0:
            return int(current) // x                
        for digit in '9':
            next_num = current + digit
            next_remainder = int(next_num) % x
            if next_remainder not in visited:
                visited.add(next_remainder)
                queue.append(next_num)    
    return -1