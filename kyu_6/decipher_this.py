# You are given a secret message you need to decipher.
# Here are the things you need to know to decipher it:
#
# For each word:
#
#     the second and the last letter is switched (e.g. Hello becomes Holle)
#     the first letter is replaced by its character code (e.g. H becomes 72)
#
# Note: there are no special characters used, only letters and spaces
#
# Examples
#
# decipherThis('72olle 103doo 100ya'); // 'Hello good day'
# decipherThis('82yade 115te 103o'); // 'Ready set go'


def decipher_this(string):
    result = []
    words = string.split()
    print(words)
    for word in words:
        number = ''
        letters = []

        for i in word:
            if i.isdigit():
                number += i
            else:
                letters.append(i)

        number = int(number)
        pre = chr(number)

        if len(letters) > 0:
            tmp = letters[0]
            letters[0] = letters[-1]
            letters[-1] = tmp

        post = ''.join(letters)

        result.append(pre + post)

    return ' '.join(result)



print(decipher_this('72olle 103doo 100ya')) # 'Hello good day'
print(decipher_this('65 119esi 111dl 111lw 108dvei 105n 97n 111ka'))

# decipherThis('82yade 115te 103o'); // 'Ready set go'