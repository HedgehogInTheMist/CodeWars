```
Implement String#whitespace?(str) (Ruby), String.prototype.whitespace(str) (JavaScript), String::whitespace(str) (CoffeeScript), or whitespace(str) (Python), which should return true/True if given object consists exclusively of zero or more whitespace characters, false/False otherwise.
```
import re

def whitespace(string: str) -> bool:
    return bool(re.match(r'^\s*$', string))