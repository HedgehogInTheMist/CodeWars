```
Create a function that takes index [0, 8] and a character. It returns a string with columns. Put character in column marked with index.

Ex.: index = 2, character = 'B'

| | |B| | | | | | |
 0 1 2 3 4 5 6 7 8
Assume that argument index is integer [0, 8]. Assume that argument character is string with one character.


```

def build_row_text(index: int, character: str):
    original_string = '| | | | | | | | |'
    return original_string[:index*2 + 1] + character + original_string[index*2:]
