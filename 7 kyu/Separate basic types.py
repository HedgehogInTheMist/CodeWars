```
Given: a sequence of different type of values (number, string, boolean). You should return an object with a separate properties for each of types presented in input. Each property should contain an array of corresponding values.
keep order of values like in input array
if type is not presented in input, no corresponding property are expected
So, for this input:
['a', 1, 2, False, 'b']
expected output is:

{
  int: [1, 2],
  str: ['a', 'b'],
  bool: [False]
}
```

def separate_types(seq: list) -> dict:
    types = {k: [item for item in seq if type(item) == k] for k in (int, str, bool)}
    return {k: v for k, v in types.items() if v}