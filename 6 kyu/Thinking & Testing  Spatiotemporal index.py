import re

def testit(a: list) -> list:
    long_measure = { 'mm': 1, 'cm': 10, 'dm': 100, 'm': 1000, 'km': 1000000 }
    time_measure = { 'ms': 1, 's': 1000, 'm': 60000, 'h': 3600000, 'd': 86400000}
    
    splitted = [split_digits_and_letters(i) for i in a]
    
    long_check = [True if i[1] in long_measure else False for i in splitted]
    time_check = [True if i[1] in time_measure else False for i in splitted]
    
    
    if all(time_check):
        unsorted = {int(i[0]) * time_measure.get(i[1]):i[1] for i in splitted}
        sorted_dict = dict(sorted(unsorted.items()))
        sorted_keys = [f"{key // time_measure.get(value)}{value}" for key, value in sorted_dict.items()]
        return sorted_keys
    elif all(long_check):
        unsorted = {int(i[0]) * long_measure.get(i[1]):i[1] for i in splitted}
        sorted_dict = dict(sorted(unsorted.items()))
        sorted_keys = [f"{key // int(long_measure.get(value))}{value}" for key, value in sorted_dict.items()]
        return sorted_keys
    else:
        if not all(long_check) and not all(time_check):
            return None
    
    
def split_digits_and_letters(input_string):
    match = re.match(r'(\d+)([a-z]+)', input_string)    
    if match:
        digits = match.group(1)
        letters = match.group(2)
        return digits, letters
    else:
        return None, None