# You are given an array(list) strarr of strings and an integer k.
# Your task is to return the first longest string consisting of k consecutive strings taken in the array.

# Examples:
#
# strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2
#
# Concatenate the consecutive strings of strarr by 2, we get:
#
# treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
# folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
# trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
# blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
# abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]
#
# Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
# The first that came is "folingtrashy" so
# longest_consec(strarr, 2) should return "folingtrashy".
#
# In the same way:
# longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
#
# n being the length of the string array, if n = 0 or k > n or k <= 0 return "".
# Note
#
# consecutive strings : follow one after another without an interruption

strarr = ["it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"]


def longest_consec(strarr, k):
    if len(strarr) == 0 or len(strarr) < k or k <= 0:
        return ''

    result = strarr[0]
    for index, element in enumerate(strarr):
        # stop loop not to go over it
        if index == len(strarr) - k + 1:
            break
        # count len of next k
        length = 0
        for i in range(k):
            length += len(strarr[index + i])
        if length > len(result):
            result = ''
            for i in range(k):
                result += strarr[index + i]
    return result


print(longest_consec(strarr, 3))
# ixoyx3452zzzzzzzzzzzz