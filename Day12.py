def convert(char):
    if char == "S":
        return -1
    elif char == "E":
        return 42
    else:
        return "abcdefghijklmnopqrstuvwxyz".index(char)

def parse():
    with open("Day12input.txt", "r") as file:
        matrix = []
        for line in file:
            matrix.append([])
            line = line.strip()
            for char in line:
                val = convert(char)
                matrix[-1].append(val)
        return matrix

def part1(m):
    visited = [0] * len(m)
    for i in range(len(m)):
        visited[i] = [0] * len(m[0])
    q = []
    found = False
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == -1:
                m[i][j] = 0
                visited[i][j] = 1
                q.append([i, j, 0, 0])
            if m[i][j] == 42:
                m[i][j] = 25
                visited[i][j] = -1
    
    while len(q) > 0:
        item = q.pop(0)
        i, j, h, d = item

        if i > 0:
            if m[i - 1][j] - h <= 1 and visited[i - 1][j] <= 0:
                q.append([i - 1, j, m[i - 1][j], d + 1])
                if visited[i - 1][j] == -1:
                    return d + 1
                visited[i - 1][j] = 1

        if i < len(m) - 1:
            if m[i + 1][j] - h <= 1 and visited[i + 1][j] <= 0:
                q.append([i + 1, j, m[i + 1][j], d + 1])
                if visited[i + 1][j] == -1:
                    return d + 1
                visited[i + 1][j] = 1

        if j > 0:
            if m[i][j - 1] - h <= 1 and visited[i][j - 1] <= 0:
                q.append([i, j - 1, m[i][j - 1], d + 1])
                if visited[i][j - 1] == -1:
                    return d + 1
                visited[i][j-1] = 1

        if j < len(m[i]) - 1:
            if m[i][j + 1] - h <= 1 and visited[i][j + 1] <= 0:
                q.append([i, j + 1, m[i][j + 1], d + 1])
                if visited[i][j + 1] == -1:
                    return d + 1
                visited[i][j + 1] = 1

    return 100000

def part2():
    m = parse()
    start = []
    can = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == -1:
                start = [i, j]
            elif m[i][j] == 0:
                can.append([i,j])
    low = part1(m)
    for possible in can:
        m = parse()
        m[start[0]][start[1]] = 0
        m[possible[0]][possible[1]] = -1
        temp = part1(m)
        if temp < low:
            low = temp
    return low
            


m = parse()
print(part1(m))
print(part2())
