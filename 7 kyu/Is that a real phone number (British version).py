```
Congratulations! That Special Someone has given you their phone number.
But WAIT, is it a valid number?
Your task is to write a function that verifies whether a given string contains a valid British mobile (cell) phone number or not.
If the string is a valid UK number, return "In with a chance".
If it is invalid, or if you're given an empty string, return "Plenty more fish in the sea".
A number can be valid in the following ways:
Here in the UK, mobile numbers begin with "07" followed by 9 other digits, e.g. "07454876120".
Sometimes the number is preceded by the country code, the prefix "+44", which replaces the "0" in ‘07’, e.g. "+447454876120".
And sometimes you will find numbers with dashes in-between digits or on either side, e.g. "+44--745---487-6120" or "-074-54-87-61-20-".
As you can see, dashes may be consecutive.
Good Luck Romeo/Juliette!
```

import re

def validate_number(input_string: str) -> str:
      return 'In with a chance' if re.findall(r'^(07\d{9}|\+447\d{9})$', input_string.replace('-', '')) else 'Plenty more fish in the sea'