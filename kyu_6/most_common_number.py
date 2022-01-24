# Complete the method which returns the number which is most frequent in the given input array.
# If there is a tie for most frequent number, return the largest number among them.
#
# Note: no empty arrays will be given.
# Examples
#
# [12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
# [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
# [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3

def highest_rank(arr):
    result = {}
    for i in arr:
        if i not in result.keys():
            result.setdefault(i, 0)
        else:
            result[i] += 1
    max_number = max(result.values())
    are_same = []
    for index, key in enumerate(result):
        if result[key] == max_number:
            are_same.append(list(result.keys())[index])
    max_for_real = are_same[0]
    if len(are_same) > 1:
        for x in are_same:
            if x > max_for_real:
                max_for_real = x
    return max_for_real


print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 12, 20, 20, 20, 20]))  # 12

# good to remember: list.count(2) - returns the number of times the 2 appears in the list
