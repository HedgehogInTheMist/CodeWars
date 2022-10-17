def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))


if __name__ == '__main__':
    assert (basic_op('+', 4, 7) == 11)
    assert (basic_op('-', 15, 18) == -3)
    assert (basic_op('*', 5, 5) == 25)
    assert (basic_op('/', 49, 7) == 7)


'''
Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.
Examples(Operator, value1, value2) --> output

('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7

'''
