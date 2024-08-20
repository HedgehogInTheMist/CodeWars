```
This kata is a very basic introduction to compression.

Your task is to make a program which takes in a sentence and returns a string 
which shows the unique position of each word in the sentence. If a word
appears more than once in the sentence, your string should return the position 
of the first occurrence of the word.
Unique position in this case means the position of the word excluding 
repeated words. Capitalisation of words should be accounted for: 'BEE' should
 be considered the same as 'bee'. The sentences include no punctuation.

```

def compress(sentence: str) -> str:
    sentence = sentence.lower().split()
    seen = set()
#     sett = [item for item in sentence if not (item in seen or seen.add(item))]
    sett = list(dict.fromkeys(sentence))
    result = [str(sett.index(i)) for i in sentence]
    return ''.join(result)
    