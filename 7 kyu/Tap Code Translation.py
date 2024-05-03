```
Tap code is a way to communicate using a series of taps and pauses for each letter. In this kata, we will use dots . for the taps and whitespaces for the pauses.

The number of taps needed for each letter matches its coordinates in the following polybius square (note the c/k position). Then you "tap" the row, a pause, then the column. Each letter is separated from others with a pause too.

   1  2  3  4  5
1  A  B C\K D  E
2  F  G  H  I  J
3  L  M  N  O  P
4  Q  R  S  T  U
5  V  W  X  Y  Z
Input:
A lowercase string of a single word (no whitespaces or punctuation, only letters).

Output:
The encoded string as taps and pauses.

Examples
text = "dot"
  "D" = (1, 4) = ". ...."
  "O" = (3, 4) = "... ...."
  "T" = (4, 4) = ".... ...."
  
output: ". .... ... .... .... ...."


"example" -> ". ..... ..... ... . . ... .. ... ..... ... . . ....."
"more"    -> "... .. ... .... .... .. . ....."
```

def tap_code_translation(text: str) -> str:
    
    polybius_square = {
        'A': '11', 'B': '12', 'C': '13', 'K': '13', 'D': '14', 'E': '15',
        'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '25', 'L': '31',
        'M': '32', 'N': '33', 'O': '34', 'P': '35', 'Q': '41', 'R': '42',
        'S': '43', 'T': '44', 'U': '45', 'V': '51', 'W': '52', 'X': '53',
        'Y': '54', 'Z': '55', ' ': '/'
    }

    encoded_message =' '.join([polybius_square[letter] for letter in text.upper() if letter in polybius_square])
    tap_code_result = ' '.join(int(i)*'.' for i in encoded_message if i.isdigit())
    return tap_code_result