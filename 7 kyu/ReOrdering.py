```
There is a sentence which has a mistake in its ordering.
The part with a capital letter should be the first word.
Please build a function for re-ordering
Examples
>>> re_ordering('ming Yao')
'Yao ming'
>>> re_ordering('Mano donowana')
'Mano donowana'
>>> re_ordering('wario LoBan hello')
'LoBan wario hello'
>>> re_ordering('bull color pig Patrick')
'Patrick bull color pig'
```

def re_ordering(text):
    words = text.split()
    for word in words:
        if word[0].istitle():
            words.remove(word)
            words.insert(0, word)
    return ' '.join(words)

