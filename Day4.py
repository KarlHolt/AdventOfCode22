with open("Day4input.txt", "r") as file:
    Total = 0
    for line in file:
        pair = line.split(",")
        start1,end1 = pair[0].split("-")
        start2,end2 = pair[1].split("-")
        one = range(int(start1), int(end1) + 1)
        two = range(int(start2), int(end2) + 1)

        for x in one:
            if x in two:
                Total += 1
                break
    print(Total)
