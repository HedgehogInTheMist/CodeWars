```
No Story
No Description
Only by Thinking and Testing
Look at result of testcase, guess the code!
```

def testit(actions: list, sample: str) -> str:
    transform = {
        'run_': '_',
        'run|': '/',
        'jump_': 'x',
        'jump|': '|'
    }
    semi_result = [''.join(i) for i in list((i,j) for i, j in zip(actions, list(sample)))]
    return ''.join([transform.get(i) for i in semi_result])
