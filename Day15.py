import re

def parse(filename):
    SB = []
    with open(filename, "r") as file:
        for line in file:
            x,y,a,b = re.findall("[-0-9]+", line)
            SB.append([[int(x), int(y)], [int(a), int(b)]])
        return SB

def dist(X, Y):
    return abs(X[0] - Y[0]) + abs(X[1] - Y[1])

def part1(SB, y_check=2000000, min_x=-1000000000, max_x=10000000000):
    xs = set()
    for sig, bea in SB:
        temp = dist(sig, bea)
        diff = temp - dist(sig, [sig[0], y_check])
        if temp > 0:
            t_1 = sig[0] - diff
            t_2 = sig[0] + diff
            if t_1 < min_x:
                t_1 = min_x
            if t_2 > max_x:
                t_2 = max_x
            for x in range(t_1, t_2):
                xs.add(x)
    return xs

def score2(x, y):
    return x * 4000000 + y

def part2(SB):
    max_x = max_y = 4000000
    for sig, bea in SB:
        temp = dist(sig, bea) + 1
        for i in range(0, temp + 1):
            tb1 = False
            tb2 = False
            tb3 = False
            tb4 = False
            t1 = [sig[0] + temp - i, sig[1] + i]
            t2 = [sig[0] + temp - i, sig[1] - i]
            t3 = [sig[0] - temp + i, sig[1] + i]
            t4 = [sig[0] - temp + i, sig[1] - i]
            if t1[0] >= 0 and t1[0] <= max_x and t1[1] >= 0 and t1[1] <= max_y:
                tb1 = True
            if t2[0] >= 0 and t2[0] <= max_x and t2[1] >= 0 and t2[1] <= max_y:
                tb2 = True
            if t3[0] >= 0 and t3[0] <= max_x and t3[1] >= 0 and t3[1] <= max_y:
                tb3 = True
            if t4[0] >= 0 and t4[0] <= max_x and t4[1] >= 0 and t4[1] <= max_y:
                tb4 = True
            for sig1, bea1 in SB:
                if tb1 == tb2 == tb3 == tb4 == False:
                    break
                temp1 = dist(sig1, bea1)
                if tb1 and dist(sig1, t1) < temp1:
                    tb1 = False
                if tb2 and dist(sig1, t2) < temp1:
                    tb2 = False
                if tb3 and dist(sig1, t3) < temp1:
                    tb3 = False
                if tb4 and dist(sig1, t4) < temp1:
                    tb4 = False
            if tb1:
                x,y = t1
            if tb2:
                x,y = t2
            if tb3:
                x,y = t3
            if tb4:
                x,y = t4

            if tb1 or tb2 or tb3 or tb4:
                return score2(x,y)
    return 0
    

sb = parse("Day15input.txt")
print(len(part1(sb)))
print(part2(sb))
