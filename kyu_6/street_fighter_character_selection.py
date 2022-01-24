# The Kata
#
# You'll have to simulate the video game's character selection screen behaviour.
#
# Input
#     the list of game characters in a 2x6 grid;
#     the initial position of the selection cursor (top-left is (0,0));
#     a list of moves of the selection cursor (which are up, down, left, right);
# Output
#     the list of characters who have been hovered by the selection cursor after all the moves
#     (ordered and with repetition, all the ones after a move, wether successful or not, see tests);
# Rules
#   selection cursor is circular horizontally but not vertically!
#   as you might remember from the game, the selection cursor rotates horizontally but not vertically;
#   that means that if I'm in the leftmost and I try to go left again I'll get to the rightmost
#   and vice versa from rightmost to leftmost.

#   instead, if I try to go further up from the upmost or further down from the downmost,
#   I'll just stay where I am located:
#   you can't go lower than lowest row:
#   you can't go upper than highest row:
#
#   For this easy version the fighters grid layout and the initial position will always be the same in all tests,
#   only the list of moves change.
#
# Notice: changing some of the input data might not help you.
#
# Examples
#
# 1.
#
# fighters = [
#     ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
#     ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
# ]
# initial_position = (0,0)
# moves = ['up', 'left', 'right', 'left', 'left']
#
# then I should get:
#
# ['Ryu', 'Vega', 'Ryu', 'Vega', 'Balrog']
#
# as the characters I've been hovering with the selection cursor during my moves.
# Notice: Ryu is the first just because it "fails" the first up See test cases for more examples.
#
# 2.
#
# fighters = [
#     ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
#     ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
# ]
# initial_position = (0,0)
# moves = ['right', 'down', 'left', 'left', 'left', 'left', 'right']
#
# Result:
#
# ['E.Honda', 'Chun Li', 'Ken', 'M.Bison', 'Sagat', 'Dhalsim', 'Sagat']

def street_fighter_selection(fighters, initial_position, moves):

    result = []

    if moves == []:
        return result

    x = initial_position[0]  # 0
    y = initial_position[1]  # 0

    for move in moves:
        if move == 'right':
            x += 1
            if x > 5:
                x = 0
        elif move == 'left':
            x -= 1
            if x < 0:
                x = 5
        elif move == 'up':
            y -= 1
            if y < 0:
                y = 0
        elif move == 'down':
            y += 1
            if y > 1:
                y = 1
        result.append(fighters[y][x])

    return result

fighters = [
	["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
	["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]

moves =  ["left"]*8

print(street_fighter_selection(fighters, (0, 0), moves))
