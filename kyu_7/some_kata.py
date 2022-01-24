# This time no story, no theory. The examples below show you how to write function accum:
# Examples:
#
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
#
# The parameter of accum is a string which includes only letters from a..z and A..Z.
test = 'cwAt'


def accum(s):
    result = str()
    start = 1
    for item in s:
        result += item.upper() + item.lower() * (start - 1)
        start += 1
        if start - 1 != len(s):
            result += '-'
    return result


print(accum(test))


# You probably know the "like" system from Facebook and other pages.
# People can "like" blog posts, pictures or other items.
# We want to create the text that should be displayed next to such an item.
#
# Implement the function which takes an array containing the names of people that like an item.
# It must return the display text as shown in the examples:
#
# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
#
# Note: For 4 or more names, the number in "and 2 others" simply increases.


def likes(name):
    if len(name) == 0:
        return 'no one likes this'
    elif len(name) == 1:
        return name[0] + ' likes this'
    elif len(name) == 2:
        return name[0] + ' and ' + name[1] + ' like this'
    elif len(name) == 3:
        return name[0] + ', ' + name[1] + ' and ' + name[2] + ' like this'
    else:
        return name[0] + ', ' + name[1] + ' and ' + str(len(name) - 2) + ' others like this'


test = ["Alex", "Jacob", "Mark", "Max"]
# solved
print(likes(test))

# other solution
def likes(names):
    formats = {
            0: "no one likes this",
            1: "{} likes this",
            2: "{} and {} like this",
            3: "{}, {} and {} like this",
            4: "{}, {} and {others} others like this"
        }
    n = len(names)
    return formats[min(n, 4)].format(*names, others=n-2)



# Given an array of ones and zeroes, convert the equivalent binary value to an integer.
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
# However, the arrays can have varying lengths, not just limited to 4.


def binary_array_to_number(arr):
    number = 0
    for index, element in enumerate(arr):
        number += (2**index)*arr[-index-1]
    return number


# this is clever, but I don't understand this
# def binary_array_to_number(arr):
#   return int("".join(map(str, arr)), 2)

a = [0, 0, 0, 1] # 1
b = [0, 0, 1, 0] # 2
c = [1, 1, 0, 0] # 12

print(binary_array_to_number(a))
print(binary_array_to_number(b))
print(binary_array_to_number(c))