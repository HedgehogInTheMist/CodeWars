```
Implement String#eight_bit_number?, which should return true if given object is a number representable by 8 bit unsigned integer (0-255), false otherwise.
It should only accept numbers in canonical representation, so no leading +, extra 0s, spaces etc.
```
import re

def eight_bit_number(n: str) -> bool:
    return bool(re.match(r'^(0|[1-9][0-9]{0,2})$', n)) and 0 <= int(n) <= 255 and '\n' not in n   
