# Build Tower
#
# Build Tower by the following given argument:
# number of floors (integer and always greater than 0).
#
# for example, a tower of 3 floors looks like below
#
# [
#   '  *  ',
#   ' *** ',
#   '*****'
# ]
#
# and a tower of 6 floors looks like below
#
# [
#   '     *     ',
#   '    ***    ',
#   '   *****   ',
#   '  *******  ',
#   ' ********* ',
#   '***********'
# ]

def tower_builder(n_floors):
    tower = []
    star = '*'
    empty_space = n_floors * 2 - 2
    half = int(empty_space / 2)
    for i in range(n_floors):
        text = half * ' ' + star + half * ' '
        tower.append(text)
        half -= 1
        star = '*' + star + '*'
    return tower


print(tower_builder(3))
