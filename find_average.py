def find_average(numbers):
    return sum([x for x in numbers]) / len(numbers)

if __name__ == '__main__':
    assert(find_average([1, 2, 3]) == 2)