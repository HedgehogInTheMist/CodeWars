```
Story
Once Mary heard a famous song, and a line from it stuck in her head. 
That line was "Will you still love me when I'm no longer young and beautiful?". 
Mary believes that a person is loved if and only if he/she is both young and beautiful, 
but this is quite a depressing thought, so she wants to put her belief to the test.

Task
Knowing whether a person is young, beautiful and loved, find out if they contradict Mary's belief.

A person contradicts Mary's belief if one of the following statements is true:
they are young and beautiful but not loved;
they are loved but not young or not beautiful.
Example
For young = true, beautiful = true and loved = true, the output should be false.
```

def will_you(young: bool, beautiful: bool, loved: bool) -> bool:
    return (young and beautiful and not loved) or (loved and (not young or not beautiful))    