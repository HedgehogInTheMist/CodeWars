```
Finding your seat on a plane is never fun, particularly for a long haul flight... You arrive, realise again just how little leg room you get, and sort of climb into the seat covered in a pile of your own stuff.
To help confuse matters (although they claim in an effort to do the opposite) many airlines omit the letters 'I' and 'J' from their seat naming system.
the naming system consists of a number (in this case between 1-60) that denotes the section of the plane where the seat is (1-20 = front, 21-40 = middle, 40+ = back). This number is followed by a letter, A-K with the exclusions mentioned above.
Letters A-C denote seats on the left cluster, D-F the middle and G-K the right.
Given a seat number, your task is to return the seat location in the following format:
'2B' would return 'Front-Left'.
If the number is over 60, or the letter is not valid, return 'No Seat!!'.
```

def plane_seat(a: str) -> str:
    front_middle_back = {range(1, 21): 'Front', range(21, 41): 'Middle', range(41, 61): 'Back'}
    left_middle_right = {'ABC': 'Left', 'DEF': 'Middle', 'GHK': 'Right'}

    seat_num, seat_letter = int(a[:-1]), a[-1].upper()

    if seat_num > 60 or seat_letter not in 'ABCDEFGHK':
        return 'No Seat!!'

    seat_position = [
        pos for numbers, pos in front_middle_back.items() if seat_num in numbers
    ] + ['-'] + [
        pos for seats, pos in left_middle_right.items() if seat_letter in seats
    ]

    return ''.join(seat_position)

