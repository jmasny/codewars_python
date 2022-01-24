# Write a function that takes an array of numbers (integers for the tests) and a target number.
# It should find two different items in the array that, when added together, give the target value.
# The indices of these items should then be returned in a tuple like so: (index1, index2).
#
# For the purposes of this kata, some tests may have multiple answers;
# any valid solutions will be accepted.
#
# The input will always be valid (numbers will be an array of length 2 or greater, and all
# of the items will be numbers; target will always be the sum of two different items from that array).

# twoSum [1, 2, 3] 4 === (0, 2)


def two_sum(numbers, target):
    for index, i in enumerate(numbers):
        for yndex, y in enumerate(numbers):
            if index == yndex:
                continue
            if i + y == target:
                return [index, yndex]


print(two_sum([1, 2, 3], 4))  # [0, 2]

# passed, but imo it's not efficient
