def HQ9(code: str) -> str:
    def compose_lyrics():
        lyrics, repetetive_verses, final_verses = "", "", ""
        for amount in range(99, 2, -1):
            repetetive_verses += f"{amount} bottles of beer on the wall, {amount} bottles of beer.\nTake one down and pass it around, {amount - 1} bottles of beer on the wall.\n"
        final_verses += "2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall."
        lyrics = repetetive_verses + final_verses
        return lyrics

    interpretation = {
        'H': 'Hello World!',
        'Q': 'Q',
        '9': compose_lyrics()
    }
    return interpretation.get(code, None)

'''
You task is to implement an simple interpreter for the notorious esoteric language HQ9+ that will work for a single character input:

    If the input is 'H', return 'Hello World!'
    If the input is 'Q', return the input
    If the input is '9', return the full lyrics of 99 Bottles of Beer. It should be formatted like this:

99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall.
98 bottles of beer on the wall, 98 bottles of beer.
Take one down and pass it around, 97 bottles of beer on the wall.
97 bottles of beer on the wall, 97 bottles of beer.
Take one down and pass it around, 96 bottles of beer on the wall.

'''