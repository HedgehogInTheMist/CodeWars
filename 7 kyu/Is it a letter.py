```
Write a function, isItLetter or is_it_letter or IsItLetter, which tells us if a given character is a letter or not.
```

import string

def is_it_letter(s: str) -> bool:
    return s in string.ascii_letters