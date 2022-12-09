def pos_to_string(pos):
    if len(pos) != 2:
        return ""
    return str(pos[0]) + "," + str(pos[1])

def dist(pos_h, pos_t):
    x, y = pos_h
    a, b = pos_t
    
    if abs(x - a) + abs(y - b) <= 1:
        return 1
    if abs(x - a) == 1 and abs(y - b) == 1:
        return 1
    else:
        return 2

def move_h(pos_h, direction):
    if direction == "R":
        pos_h[0] += 1
    elif direction == "U":
        pos_h[1] += 1
    elif direction == "L":
        pos_h[0] -= 1
    elif direction == "D":
        pos_h[1] -= 1
    else:
        raise "Wrong input for move h"

def move_t(pos_t, pos_h):
    x,y = pos_h
    a,b = pos_t

    if y > b:
        pos_t[1] += 1
    elif y < b:
        pos_t[1] += -1
    if x > a:
        pos_t[0] += 1
    elif x < a:
        pos_t[0] += -1

def part1():
    with open("Day9input.txt", "r") as file:
        pos_h = [0, 0]
        pos_t = [0, 0]
        visited = {pos_to_string(pos_t)}
        for line in file:
            line = line.strip()
            direction, number = line.split(" ")

            for i in range(int(number)):
                move_h(pos_h, direction)
                if dist(pos_h, pos_t) > 1:
                    move_t(pos_t, pos_h)
                    visited.add(pos_to_string(pos_t))
        return len(visited)

def part2():
    with open("Day9input.txt", "r") as file:
        pos = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
        visited = {pos_to_string([0,0])}
        for line in file:
            line = line.strip()
            direction, number = line.split(" ")

            for i in range(int(number)):
                move_h(pos[0], direction)
                for j in range(1, len(pos)):
                    if dist(pos[j], pos[j-1]) > 1:
                        move_t(pos[j], pos[j-1])
                        if j == 9:
                            visited.add(pos_to_string(pos[j]))
        return len(visited)

print(part1())
print(part2())
