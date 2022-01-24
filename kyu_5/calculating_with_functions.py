# This time we want to write calculations using functions and get the results. Let's have a look at some examples:
#
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
#
# Requirements:
#
#     There must be a function for each number from 0 ("zero") to 9 ("nine")
#     There must be a function for each of the following mathematical operations:
#     plus, minus, times, dividedBy (divided_by in Ruby and Python)
#     Each calculation consist of exactly one operation and two numbers
#     The most outer function represents the left operand, the most inner function represents the right operand
#     Division should be integer division. For example, this should return 2, not 2.666666...:
#
# eight(divided_by(three()))

def calculate(first, operator, second):
    if operator == '+':
        return int(first + second)
    elif operator == '-':
        return int(first - second)
    elif operator == '*':
        return int(first * second)
    elif operator == '/':
        return int(first / second)
    else:
        return -1


def zero(*args):
    if len(args) == 0:
        return 0
    else:
        first = 0
        operator = args[0][0]
        second = args[0][1]
        return calculate(first, operator, second)

def one(*args):
    if len(args) == 0:
        return 1
    else:
        first = 1
        operator = args[0][0]
        second = args[0][1]
        return calculate(first, operator, second)


def two(*args):
    if len(args) == 0:
        return 2
    else:
        first = 2
        operator = args[0][0]
        second = args[0][1]
        return calculate(first, operator, second)


def three(*args):
    if len(args) == 0:
        return 3
    else:
        first = 3
        operator = args[0][0]
        second = args[0][1]
        return calculate(first, operator, second)


def four(*args):
    if len(args) == 0:
        return 4
    else:
        first = 4
        operator = args[0][0]
        second = args[0][1]
        return calculate(first, operator, second)


def five(*args):
    if len(args) == 0:
        return 5
    else:
        first = 5
        operator = args[0][0]
        second = args[0][1]
        return calculate(first, operator, second)


def six(*args):
    if len(args) == 0:
        return 6
    else:
        first = 6
        operator = args[0][0]
        second = args[0][1]
        return calculate(first, operator, second)


def seven(*args):
    if len(args) == 0:
        return 7
    else:
        first = 7
        operator = args[0][0]
        second = args[0][1]
        return calculate(first, operator, second)


def eight(*args):
    if len(args) == 0:
        return 8
    else:
        first = 8
        operator = args[0][0]
        second = args[0][1]
        return calculate(first, operator, second)


def nine(*args):
    if len(args) == 0:
        return 9
    else:
        first = 9
        operator = args[0][0]
        second = args[0][1]
        return calculate(first, operator, second)


def plus(number):  # your code here
    return ['+',number]


def minus(number):  # your code here
    return ['-', number]


def times(number):  # your code here
    return ['*', number]


def divided_by(number):  # your code here
    return ['/', number]

print(eight(minus(three())))