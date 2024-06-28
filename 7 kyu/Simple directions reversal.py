```
In this Kata, you will be given directions and your task will be to find your way back.

solve(["Begin on Road A","Right on Road B","Right on Road C","Left on Road D"]) = ['Begin on Road D', 'Right on Road C', 'Left on Road B', 'Left on Road A']
solve(['Begin on Lua Pkwy', 'Right on Sixth Alley', 'Right on 1st Cr']) =  ['Begin on 1st Cr', 'Left on Sixth Alley', 'Left on Lua Pkwy']
More examples in test cases.

Good luck!

Please also try Simple remove duplicates
```

def solve(arr: list) -> list:
    directions = [i.split()[0] for i in arr][::-1]
    roads = [' '.join(i.split()[1:]) for i in arr[::-1]]
    directions = ['Right' if direction == 'Left' else 'Left' if direction == 'Right' else direction for direction in directions]
    correct_directions = [directions[-1]] + directions[:-1]
    return list(i + ' ' + j for i, j in zip(correct_directions, roads))
    
