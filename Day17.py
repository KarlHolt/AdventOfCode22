def parse():
    with open("Day17input.txt", "r") as file:
        output = []
        for line in file:
            for char in line:
                if char in ["<", ">"]:
                    output.append(char)
        return output

def get_rock_shape(rock_type):
    shape = []
    if rock_type == "_":
        shape = [[".", ".", "#", "#", "#", "#", "."]]
    elif rock_type == "+":
        shape = [[".", ".", ".", "#", ".", ".", "."],
                 [".", ".", "#", "#", "#", ".", "."],
                 [".", ".", ".", "#", ".", ".", "."]
                ]
    elif rock_type == "L":
        shape = [[".", ".", ".", ".", "#", ".", "."],
                 [".", ".", ".", ".", "#", ".", "."],
                 [".", ".", "#", "#", "#", ".", "."]
                ]
    elif rock_type == "l": #Small "L"
        shape = [[".", ".", "#", ".", ".", ".", "."],
                 [".", ".", "#", ".", ".", ".", "."],
                 [".", ".", "#", ".", ".", ".", "."],
                 [".", ".", "#", ".", ".", ".", "."]
                ]
    elif rock_type == "#":
        shape = [[".", ".", "#", "#", ".", ".", "."],
                 [".", ".", "#", "#", ".", ".", "."]
                ]
    return shape

def push_rock(rock, wind_direction):
    if wind_direction == ">":
        space = True
        for row in rock:
            if row[-1] == "#":
                space = False
        if space:
            for row in rock:
                length = len(row)
                for i in range(len(row) - 1):
                    row[length - i] = row[length - i - 1]
    elif wind_direction == "<":
        shace = True
        for row in rock:
            if row[0] == "#":
                space = False
        if space:
            for row in rock:
                for i in range(len(row) - 1):
                    rock[i] = rock[i + 1]

def space_to_move_rock(rock, wind_blow, board):
    height_rock = len(rock)
    

def collusion(rock, board, height):
    pass

def part1(winds, n_rocks):
    rock_types = ["_", "+", "L", "l", "#"] # The 4th rock is lowercase "L"
    board = ["#"] * 7

    j = 0
    for ith_rock in range(n_rocks):
        current_rock = rock_types[ith_rock % len(rock_types)]
        rock = get_rock_shape(current_rock)
        touch = False
        height = -3
        while not touch:
            wind_blow = winds[j % len(winds)]
            j += 1
            if height >= 0:
                space = space_to_move_rock(rock, wind_blow, board)
                if space:
                    push_rock(rock, wind_blow)
                collude = collusion(rock, board, height)
                height += 1
                if collude:
                    touch = True

winds = parse()
print(part1(winds, 10))
