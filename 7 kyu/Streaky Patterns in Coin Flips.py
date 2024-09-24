```
Credits go to the fantastic Numberphile YouTube channel for the inspiration behind this kata - the specific video for it can be found here: https://www.youtube.com/watch?v=tP-Ipsat90c&t=545s

Your challenge in this Kata is to code a function check_sequence that checks a sequence of coin flip results for specific 'streak' patterns of Heads and Tails. Streaks are consecutive occurences of results -- a streak of length 3 would be 'HHH' or 'TTT'.

Given a sequence such as 'HTHHHHTTH', an integer l, and integer n, we want to check the existence of STRICTLY n-number of streaks that are STRICTLY of length l in the sequence.

By STRICTLY of a certain length, we mean that those streaks are not greater than or less than that length l. For instance, sequences such as 'HHHH' or 'TTTT' are streaks of length 4, and do not count as streaks of length 3, 2, or 1 even though those streaks might be contained within them.

Likewise, we are looking for STRICTLY n occurences of streaks of a given length -- NOT more or less than the value of N.

The function check_sequence should return True if the sequence conforms to this pattern, or False otherwise.

For example, check_sequence('HTHHHTTH', 3, 1) should return True, because there is 1 streak of exactly length 3 ('HHH'). Likewise, check_sequence('HTHHHTTTHHHHT', 3, 2) should return True because there exists 2 streaks of exactly length 3 ('HHH' and 'TTT').

Test cases are a mix of static cases and randomly generated cases. For the randomly generated cases:

Coin flip sequences (e.g. 'HTHHT') are from character lengths of 5 to 70 inclusive
L can take any integer value from 2 to 8 inclusive
N can take any integer value from 1 to 8 inclusive
```
import re

def check_sequence(sequence, l, n):
    return list(map(len, re.findall(r'H+|T+', sequence))).count(l)==n