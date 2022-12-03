import time

def char_value(A):
    AI = ord(A)
    if AI < 97:
        return AI - 64 + 26
    else:
        return AI - 96

def part1():
    with open("Day3input.txt", "r") as file:
        Total = 0
        for line in file:
            line = line.strip()
            
            half = len(line)//2

            first = sorted(line[0:half])
            second = sorted(line[half:])
            
            i=j=0
            while True:
                if first[i] == second[j]:
                    Total += char_value(first[i])
                    break
                elif first[i] > second[j] and j < half - 1:
                    j += 1
                elif first[i] < second[j] and i < half - 1:
                    i += 1
                else:
                    break
        return Total

def part2():
    with open("Day3input.txt", "r") as file:
        Total = 0
        a = 0
        lines = ["", "", ""]
        for line in file:
            if a < 3:
                lines[a] = sorted(line)[1:]
                a+=1
                if a < 3:
                    continue
            a = 0

            i=j=k=0
            while True:
                if lines[0][i] == lines[1][j] == lines[2][k]:
                    Total += char_value(lines[0][i])
                    break
                minchar = min(lines[0][i], lines[1][j], lines[2][k])
                if minchar == lines[0][i]:
                    i+=1
                elif minchar == lines[1][j]:
                    j+=1
                else:
                    k+=1
        return Total


now = time.time()
print("part 1: ", part1())
print(time.time() - now)

now = time.time()
print("part 2:", part2())
print(time.time() - now)
