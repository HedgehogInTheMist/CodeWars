```
DESCRIPTION:
Inside of the city there are many gangs, each with differing numbers of members wielding different weapons and possessing different strength levels. The gangs do not really want to fight one another, and so the "If you can't beat 'em, join 'em" rule applies. The gangs start combining with the most powerful gangs being joined by the weaker gangs until there is one gang left.

Challenge:

You are given a list of lists. Inside of the interior lists are numbers. Join the lists together by descending total list value ending up with one final list.

Simple example:

cant_beat_so_join([[1,2], [3,4], [5,6], [7,8], [9]]) -> [7, 8, 5, 6, 9, 3, 4, 1, 2]
In the example above, [7, 8] are the first in the list because they have the highest value
They are followed by [5, 6]
That is followed by [9] which comes before [3, 4] because the list of [9] is greater
It ends with [1, 2] which has the least amount of value
More examples:

cant_beat_so_join([[5, 1],[9, 14],[17, 23],[4, 1],[0, 1]]) -> [17, 23, 9, 14, 5, 1, 4, 1, 0, 1]
cant_beat_so_join([[13, 37], [43, 17], [2,3], [45,64], [1,9]]) -> [45, 64, 43, 17, 13, 37, 1, 9, 2, 3]
cant_beat_so_join([[], [], [], []]) -> []
cant_beat_so_join([[], [], [0], []]) -> [0]
cant_beat_so_join([[1,0,1,0,1,0], [0,1,0,0,1,0,0,1], [0], []]) -> [1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]
In the case of more than one list sharing the same sum, place them in the same order that they were in the argument:

cant_beat_so_join([[0,1,1,1], [1,0,1,1], [1,1,0,1], [3]]) -> [0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 3]
```

def cant_beat_so_join(numbers: list) -> list:
    return sum(sorted(numbers,key = lambda lst: sum(lst),reverse = True),[])