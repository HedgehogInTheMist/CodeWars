```
An array of arrays is referred to as jagged if its subarrays have varying lengths. However, in certain scenarios, you might need to normalize a jagged array. Normalizing, in this context, involves transforming it into a rectangular matrix of dimensions N x M, where N represents the number of subarrays and M represents the length of the longest subarray. This transformation is achieved by padding shorter subarrays with a specified value (passed as an argument) until they match the length of the longest subarray.

# normalizing the array with value None (python example)

[
[1, 2, 3],
[4],
[5, 6, 7, 8]
]
will turn into:

[
[1, 2, 3, None],
[4, None, None, None],
[5, 6, 7, 8]
]
Your task
Implement a function that accepts a jagged array as input and returns its normalized version.

Notes
All inputs are valid jagged arrays containing N subarrays, where 0 ≤ N ≤ 15, with integers ranging from 0 to 9.
The fill value for padding can vary and will be specified in the function's signature.
There are 100 random tests.

```

def normalize(arr: list, fill_value=None):
     return [i + [fill_value] * (max(len(x) for x in arr) - len(i)) for i in arr]