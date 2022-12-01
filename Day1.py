def insert_value(value, value_list):
    last = value
    for i in range(3):
        if last > value_list[i]:
            temp = value_list[i]
            value_list[i] = last
            last = temp

max_food = [0,0,0]
with open("Day1input.txt", "r") as file:
    temp = 0
    for line in file:
        if(line.strip()):
            temp += int(line)
            continue
        if temp > max_food[2]:
            insert_value(temp, max_food)
        temp = 0
    print("part 1:", max_food[0])
    print("part 2:", sum(max_food))
