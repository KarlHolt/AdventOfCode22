from functools import cmp_to_key

def parse():
    with open("Day13input.txt", "r") as file:
        pairs = []
        temp = []
        i = 0
        for line in file:
            if i < 2:
                temp.append(eval(line))
                i+=1
            else:
                i = 0
                pairs.append(temp)
                temp = []
        return pairs

def parse2():
    with open("Day13input.txt", "r") as file:
        packets = []
        i = 0
        for line in file:
            if i == 2:
                i = 0
                continue
            packets.append(eval(line))
            i+=1
        packets.append([[2]])
        packets.append([[6]])
        return packets


def check(l, r):
    if type(l) == type(r) == list:
        if len(l) == len(r) == 0:
            return -1
        elif len(l) == 0:
            return True
        elif len(r) == 0:
            return False
        for i in range(len(l)):
            if i == len(r):
                return False
            temp = check(l[i], r[i])
            if temp != -1:
                return temp
        if len(l) < len(r):
            return True
        return -1
    elif type(l) == list:
        return check(l, [r])
    elif type(r) == list:
        return check([l], r)
    else:
        if l == r:
            return -1
        return l < r

def part1(p):
    index = 1
    sum = 0
    for pair in p:
        bo = True
        left = pair[0]
        right = pair[1]

        t = check(left, right)
        if t:
           sum += index
        index += 1
    return sum

def compare(l, r):
    t = check(l, r)
    if t:
        return -1
    else:
        return 1

def part2(p):
    p = sorted(p, key=cmp_to_key(compare))
    t = 1
    index = 1
    for el in p:
        if el in [[[2]], [[6]]]:
            t *= index
        index += 1
    return t
    

p = parse()
print("part 1", part1(p))
pl = parse2()
print("part 2", part2(pl))
