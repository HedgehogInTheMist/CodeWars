```
Task
Write a function that checks if two non-negative integers make an "interlocking binary pair".

Interlock ?
numbers can be interlocked if their binary representations have no 1's in the same place
comparisons are made by bit position, starting from right to left (see the examples below)
when representations are of different lengths, the unmatched left-most bits are ignored
Examples
a = 9, b = 4
Stacking representations shows how they can interlock.

 9    1001
 4     100
Here, no 1's share any position, so the function returns true.

a = 3, b = 6
These representations do not interlock.

 3      11
 6     110
Finding they both have a 1 in the same position, the function returns false.

Input
Two non-negative integers.

Output
Boolean true or false whether or not these integers are interlockable.
```
def interlockable(a: int, b: int) -> bool:
    a = f'{a:b}'[::-1]
    b = f'{b:b}'[::-1]
    for i, el in enumerate(zip(a,b)):        
        if el[0] == el[1] == '1':
            return False
    return True    