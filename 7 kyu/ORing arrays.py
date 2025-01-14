```
It started as a discussion with a friend, who didn't fully grasp some way of setting defaults, but I thought the idea was cool enough for a beginner kata: binary OR each matching element of two given arrays (or lists, if you do it in Python; vectors in c++) of integers and give the resulting ORed array [starts to sound like a tonguetwister, doesn't it?].

If one array is shorter than the other, use the optional third parameter (defaulted to 0) to OR the unmatched elements.

For example:

or_arrays([1,2,3],[1,2,3]) == [1,2,3]
or_arrays([1,2,3],[4,5,6]) == [5,7,7]
or_arrays([1,2,3],[1,2]) == [1,2,3]
or_arrays([1,2],[1,2,3]) == [1,2,3]
or_arrays([1,2,3],[1,2,3],3) == [1,2,3]
```

def or_arrays(arr1, arr2, default=0):
    return [
        (arr1[i] if i < len(arr1) else default) | (arr2[i] if i < len(arr2) else default)
            for i in range(max(len(arr1), len(arr2)))
    ]