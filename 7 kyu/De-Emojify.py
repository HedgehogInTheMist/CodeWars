```
Inspired by the emojify custom Python module.
You are given a string made up of chains of emotes separated by 1 space each, with chains having 2 spaces 
in-between each.
Each emote represents a digit:
:)  | 0
:D  | 1
>(  | 2
>:C | 3
:/  | 4
:|  | 5
:O  | 6
;)  | 7
^.^ | 8
:(  | 9
Each emote chain represents the digits of the ASCII/Unicode code for a character, e.g. :( ;) is 97, 
which is the ASCII code for 'a'.
Given a such string of emotes, find the string it represents. Example:
':D :) :/  :D :) :|' is 2 chains: ':D :) :/' and ':D :) :|'.
These represent ASCII codes 104 and 105 respectively, translating to 'hi'.
Input will always be valid. Chains may start with leading zeroes; these are valid and do not change 
the chain's value.
```

def deemojify(emote_string: str) -> str:
    emoji_dict = {':)': 0, ':D': 1, '>(': 2, '>:C': 3, ':/': 4, ':|': 5, ':O': 6, ';)': 7, '^.^': 8, ':(': 9, ' ': ' '}
    emoji_string_to_list = emote_string.split(' ')
    sr = ''.join([str(emoji_dict.get(i)) for i in emoji_string_to_list]).replace('None', ', ').split(',')
    return ''.join([chr(int(i)) for i in sr])