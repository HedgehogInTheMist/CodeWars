```
Change every letter in a given string to the next letter in the alphabet. The function takes a single parameter s (string).
Notes:
Spaces and special characters should remain the same.
Capital letters should transfer in the same way but remain capitilized.
Examples
"Hello"               -->  "Ifmmp"
"What is your name?"  -->  "Xibu jt zpvs obnf?"
"zoo"                 -->  "app"
"zzZAaa"              -->  "aaABbb"
```

def next_letter(s: str) -> str:
    result = ''
    for char in s:
        if char.isalpha():
            if char == 'z':
                shifted = 'a'
            elif char == 'Z':
                shifted = 'A'
            else:
                shifted = chr(ord(char) + 1)
            
            if char.isupper():
                result += shifted.upper()
            else:
                result += shifted
        else:
            result += char
    return result