def parsestacks():
    with open("Day5input.txt", "r") as file:
        stacks = [[], [], [], [], [], [], [], [], []]
        parsing = True
        for line in file:
            if line == "":
                break
            if parsing == True:
                insertion = False
                for i in range(len(line)):
                    char = line[i]
                    if char == "[":
                        insertion = True
                        continue
                    if insertion == True:
                        stacks[(i - 1) // 4].append(char)
                        insertion = False
        for i in range(len(stacks)):
            stacks[i] = stacks[i][::-1]
        return stacks

def part1(stacks):
    with open("Day5input.txt", "r") as file:
        ready = False
        for line in file:
            if not ready:
                if not line.strip():
                    ready = True
                continue

            _, n, _, From, _, to = line.split(" ")
            for i in range(int(n)):
                temp = stacks[int(From) - 1].pop()
                if temp != []:
                    stacks[int(to) - 1].append(temp)
        result = ""
        for i in range(len(stacks)):
            if len(stacks[i]) > 0:
                result = result + stacks[i].pop()
        return result
def part2(stacks):
   with open("Day5input.txt", "r") as file:
        ready = False
        for line in file:
            if not ready:
                if not line.strip():
                    ready = True
                continue

            _, n, _, From, _, to = line.split(" ")

            elms = []
            for i in range(int(n)):
                temp = stacks[int(From) - 1].pop()
                elms.append(temp)
            
            for i in range(int(n)):
                temp = elms.pop()
                if temp != []:
                    stacks[int(to) - 1].append(temp)
        result = ""
        for i in range(len(stacks)):
            if len(stacks[i]) > 0:
                result = result + stacks[i].pop()
        return result 

stacks = parsestacks()
print("part1",part1(stacks))
stacks = parsestacks()
print("part2",part2(stacks))
