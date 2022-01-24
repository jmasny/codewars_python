# Longest Palindrome
#
# Find the length of the longest substring in the given string s that is the same in reverse.
#
# As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.
#
# If the length of the input string is 0, the return value must be 0.
#
# "a" -> 1
# "aab" -> 2
# "abcde" -> 1
# "zzbaabcd" -> 4
# "" -> 0

def is_palindrome(s: str):

    if s == s[::-1]:

        return True


def longest_palindrome(s):

    longest = 0

    if len(s) == 0:
        return longest

    substrings = []

    for i in range(len(s)):
        for j in range(len(s) + 1):
            substrings.append(s[i:i+j])

    for sub in substrings:
        if is_palindrome(sub):
            if len(sub) > longest:
                longest = len(sub)

    return longest


print(longest_palindrome("a"))