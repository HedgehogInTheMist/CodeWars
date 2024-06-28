```
DESCRIPTION:
In this kata you are given an array to sort but you're expected to start sorting from a specific position of the array (in ascending order) and optionally you're given the number of items to sort.

Examples:
sect_sort([1, 2, 5, 7, 4, 6, 3, 9, 8], 2) //=> [1, 2, 3, 4, 5, 6, 7, 8, 9]
sect_sort([9, 7, 4, 2, 5, 3, 1, 8, 6], 2, 5) //=> [9, 7, 1, 2, 3, 4, 5, 8, 6]
Documentation:
sect_sort(array, start, length);
array - array to sort
start - position to begin sorting
length - number of items to sort (optional)
if the length argument is not passed or is zero, you sort all items to the right of the start position in the array
```

def sect_sort(*args: list) -> list:
    print(args)
    result = []
    start = args[0][:args[1]]
    if len(args) > 2:
        print(sorted(args[0][args[1]:args[1] + args[2]]))

        sorted_part = sorted(args[0][args[1]:args[1] + args[2]])
        
        ending = args[0][args[1] + args[2]:]
#         print(ending)
        result = start + sorted_part + ending
        return result
    else:
        result = start + sorted(args[0][args[1]:])
        return result