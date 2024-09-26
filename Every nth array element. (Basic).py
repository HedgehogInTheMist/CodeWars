```
Create a function (a method in Ruby, an extension method in C#) every which returns every nth element of an array.

Usage
With one argument, every(array) returns every element of the array.

With two arguments, every(array, interval) it returns every intervalth element.

With three arguments, every(array, interval, start_index) returns every intervalth element starting at index start_index.

Examples
every([0,1,2,3,4])     -> [0,1,2,3,4]
every([0,1,2,3,4],1)   -> [0,1,2,3,4]
every([0,1,2,3,4],2)   -> [0,2,4]
every([0,1,2,3,4],3)   -> [0,3]
every([0,1,2,3,4],3,1) -> [1,4]
Notes
Test cases:

interval will always be a positive integer (but may be larger than the size of the array).
start_index will always be within the bounds of the array.
Once you have completed this kata, try the advanced version (http://www.codewars.com/kata/every-nth-array-element-advanced) which allows negative intervals and unbounded start_indexes



```
def every(array, interval=None, start_index=None) -> list:
    return array[start_index::interval]