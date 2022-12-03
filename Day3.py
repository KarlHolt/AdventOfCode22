import math

with open("Day3input.txt", "r") as file:
    Total = 0
    a = 0
    lines = ["", "", ""]
    for line in file:
        if a < 2:
            lines[a] = line
            a += 1
            continue
        if a == 2:
            lines[a] = line
        a = 0
        
        for char in lines[0]:
            if char in lines[1] and char in lines[2]:
                intchar = ord(char)
                if intchar < 97:
                    Total += intchar - 64 + 26
                else:
                    Total += intchar - 96
                break
        continue
        #Part 1
        line = line.strip()
        n = len(line)
        first = line[0:math.ceil(n/2)]
        second = line[math.floor(n/2):]

        for i in range(len(first)):
            char = first[i]
            if char in second and char not in first[:i]:
                intchar = ord(char)
                if intchar < 97:
                    Total += intchar - 64 + 26
                    break
                else: 
                    Total += intchar - 96
                    break
    print(Total)
