```
Task
We define the middle of the array arr as follows:

if arr contains an odd number of elements, its middle is the element whose index number is the same when counting from the beginning of the array and from its end;

if arr contains an even number of elements, its middle is the sum of the two elements whose index numbers when counting from the beginning and from the end of the array differ by one.

An array is called smooth if its first and its last elements are equal to one another and to the middle. Given an array arr, determine if it is smooth or not.

Example
For arr = [7, 2, 2, 5, 10, 7], the output should be true

The first and the last elements of arr are equal to 7, and its middle also equals 2 + 5 = 7. Thus, the array is smooth and the output is true.

For arr = [-5, -5, 10], the output should be false

The first and middle elements are equal to -5, but the last element equals 10. Thus, arr is not smooth and the output is false.

Input/Output
[input] integer array arr

The given array.

Constraints: 2 ≤ arr.length ≤ 103, -103 ≤ arr[i] ≤ 103.

[output] a boolean value

true if arr is smooth, false otherwise.
```

def is_smooth(arr):
    if len(arr) % 2:        
        if arr[0] == arr[len(arr)//2] == arr[-1]:
            return True
        else:
            return False
    elif not len(arr) % 2:
        if arr[0] == arr[len(arr)//2] + arr[len(arr)//2 - 1] == arr[-1]:
            return True
    return False