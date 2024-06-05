```
Everybody knows a little german, right? But remembering the correct articles is a tough job. Write yourself a little helper, that returns the noun with the matching article:

each noun containing less than 2 vowels has the article "das"
each noun containing 2/3 vowels has the article "die"
each noun containing more than 3 vowels has the article "der"
Caution: Vowels are "a,e,i,o,u". Umlaute (ä ö ü) are also being counted!

(This Kata is a joke, there is no such grammar rule!)
```

def der_die_das(wort: str) -> str:
    vowels = 'aeiouäöüAEIOU'
    count = sum([1 for i in wort if i in vowels])
    if count < 2:
        return 'das ' + wort
    elif count > 3:
        return 'der ' + wort
    else:
        return 'die ' + wort