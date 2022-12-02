def calc_score_for_round_part1(MyChoice, OpponentChoice):
    MyOptions = ["X", "Y", "Z"]
    Opponent  = ["A", "B", "C"]
    
    MyI = MyOptions.index(MyChoice)
    OpI = Opponent.index(OpponentChoice)

    if MyI == OpI:
        return 3 + MyI + 1
    elif (MyI + 1) % 3 == OpI:
        return 0 + MyI + 1
    else:
        return 6 + MyI + 1

def calc_score_for_round(MyChoice, OpponentChoice):
    Opponent = ["A", "B", "C"]
    MyOptions = ["X", "Y", "Z"]

    MyI = MyOptions.index(MyChoice)
    OpI = Opponent.index(OpponentChoice)

    if MyI == 0:
        return (OpI + 2) % 3 + 1
    elif MyI == 1:
        return 3 + OpI + 1
    else:
        return 6 + ((OpI + 1) % 3) + 1

with open("Day2input.txt", "r") as file:
    total_score = 0
    for line in file:
        O, M = line.split()
        total_score += calc_score_for_round(M, O)
    print(total_score)

