def parse():
    with open("Day14input.txt", "r") as file:
        rocks = [0] * 1000
        for i in range(1000):
            rocks[i] = set()
        up = down = 0
        left = 1000
        right = -1000
        for line in file:
            points = line.split("->")
            last = eval(points[0])
            rocks.append(last)
            for i in range(1, len(points)):
                new = eval(points[i])
                if new[0] != last[0]:
                    if new[0] > last[0]:
                        range_ = range(last[0], new[0] + 1)
                    else:
                        range_ = range(new[0], last[0] + 1)
                    for position in range_:
                        rocks[position].add(new[1])
                elif new[1] != last[1]:
                    if new[1] > last[1]:
                        range_ = range(last[1], new[1] + 1)
                    else:
                        range_ = range(new[1], last[1] + 1)
                    for position in range_:
                        rocks[new[0]].add(position)
                if new[0] < left:
                    left = new[0]
                if new[0] > right:
                    right = new[0]
                if new[1] > down:
                    down = new[1]
                last = new
        rocks[-1] = [up, down, right, left]
        return rocks

def move_sand1(pos, lowest):
    if pos[1] > lowest: return (-1, -1) #Base case
    if pos[1] + 1 not in r1[pos[0]]:
        return move_sand1((pos[0], pos[1] + 1), lowest)
    if pos[1] + 1 not in r1[pos[0] - 1]:
        return move_sand1((pos[0] - 1, pos[1] + 1), lowest)
    if pos[1] + 1 not in r1[pos[0] + 1]:
        return move_sand1((pos[0] + 1, pos[1] + 1), lowest)
    return pos

def move_sand2(pos):
    if pos[1] + 1 not in r2[pos[0]]:
        return move_sand2((pos[0], pos[1] + 1))
    if pos[1] + 1 not in r2[pos[0] - 1]:
        return move_sand2((pos[0] - 1, pos[1] + 1))
    if pos[1] + 1 not in r2[pos[0] + 1]:
        return move_sand2((pos[0] + 1, pos[1] + 1))
    if pos == (500, 0):
        return (-1, -1)
    return pos

def print_rocks(rocks):
    up, down, right, left = rocks[-1]
    for i in range(up, down+3):
        for j in range(left - 1, right + 2):
            if i in rocks[j]:
                print("#", end="")
            else:
                print(".", end="")
        print()


def part1():
    up, lowest, left, right = r1[-1]
    
    num_sand = 0
    void = False
    while not void:
        sand_pos = move_sand1((500, 0), lowest)
        if sand_pos == (-1, -1) or sand_pos == (500, 0):
            void = True
            continue
        r1[sand_pos[0]].add(sand_pos[1])
        num_sand += 1
    return num_sand

def part2():
    up, lowest, left, right = r2[-1]

    for i in range(1000):
        r2[i].add(lowest + 2)

    num_sand = 0
    void = False
    while not void:
        sand_pos = move_sand2((500, 0))
        num_sand += 1
        if sand_pos == (-1, -1):
            void = True
            continue
        r2[sand_pos[0]].add(sand_pos[1])
    return num_sand


r1 = parse()
print(part1())

r2 = parse()
print(part2())
