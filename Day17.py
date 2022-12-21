def parse():
    with open("Day17input.txt", "r") as file:
        output = []
        for line in file:
            for char in line:
                if char in ["<", ">"]:
                    output.append(char)
        return output

def part1(winds, n_rocks):
    rock_types = ["_", "+", "L", "l", "#"] # The 4th rock is lowercase "L"
    board = []
    for i in range(3):
        board.append(["."] * 7)

    board[1][2] = "%"
    
    print(board)
    for rock in range(n_rocks):
        current_rock = rock_types[rock % len(rock_types)]

winds = parse()
print(part1(winds, 10))
