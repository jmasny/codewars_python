# Write Number in Expanded Form
#
# You will be given a number and you will need to return it as a string in Expanded Form. For example:
#
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
#
# NOTE: All numbers will be whole numbers greater than 0

def expanded_form(num):
    memory = []
    multiplication = 1
    while num > 0:
        a = num % 10
        memory.append(a*multiplication)
        num = num // 10
        multiplication *= 10
    memory.reverse()
    result = ''
    for i in memory:
        if i == 0:
            continue
        if i < 10:
            result += str(i)
        else:
            result += str(i) + ' + '
    if result[-3:] == ' + ':
        return result[:-3]
    else:
        return result


print(expanded_form(184816))
print(expanded_form(2000 + 900 + 106))
print(expanded_form(8))
print(expanded_form(88))
print(expanded_form(159))
print(expanded_form(102))
print(expanded_form(1482))
print(expanded_form(70000382))
print(expanded_form(9000000))