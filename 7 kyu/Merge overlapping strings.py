```
This kata requires you to write a function which merges two strings together. It does so by merging the end of the first string with the start of the second string together when they are an exact match.

"abcde" + "cdefgh" => "abcdefgh"
"abaab" + "aabab" => "abaabab"
"abc" + "def" => "abcdef"
"abc" + "abc" => "abc"
NOTE: The algorithm should always use the longest possible overlap.

"abaabaab" + "aabaabab" would be "abaabaabab" and not "abaabaabaabab"
```

def merge_strings(first: str, second: str) -> str:
    max_overlap = 0
    for i in range(1, min(len(first), len(second)) + 1):
        if first[-i:] == second[:i]:
            max_overlap = i    
    return first + second[max_overlap:]