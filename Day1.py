def Solution1():
    max_food = 0
    with open("Day1input.txt", "r") as file:
        temp = 0
        for line in file:
            if(line.strip()):
                temp += int(line)
                continue
            if temp > max_food:
                max_food = temp
            temp = 0
    print(max_food)


Solution1()
