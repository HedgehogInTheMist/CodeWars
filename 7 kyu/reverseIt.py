```
You have to create a function named reverseIt.
Write your function so that in the case a string or a number is passed in as the data , 
you will return the data in reverse order. If the data is any other type, return it as it is.
Examples of inputs and subsequent outputs:

"Hello" -> "olleH"

"314159" -> "951413"

[1,2,3] -> [1,2,3]
```

def reverse_it(data: str) -> str:
    if type(data) == str:
        return data[::-1]
    elif type(data) == bool:
            return True
    elif type(data) == float:
        data = str(data)[::-1]
        return float(data)
    elif type(data) == int:
        data = str(data)[::-1]
        return int(data)    
    return data