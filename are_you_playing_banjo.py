def are_you_playing_banjo(name):
    return f'{name} plays banjo' if name.lower().startswith('r') else f'{name} does not play banjo'


if __name__ == '__main__':
    assert(are_you_playing_banjo('martin') == 'martin does not play banjo')
    assert(are_you_playing_banjo('Rikke') == "Rikke plays banjo");
    assert(are_you_playing_banjo("bravo") == "bravo does not play banjo")
    assert(are_you_playing_banjo("rolf") == "rolf plays banjo")