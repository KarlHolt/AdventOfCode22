def parser():
    with open("Day8input.txt", "r") as file:
        matrix = []
        for line in file:
            line = line.strip()
            temp_row = []
            
            for char in line:
                temp_row.append(int(char))

            matrix.append(temp_row)
        return matrix

def part1(matrix):
    visible = len(matrix) * 2 + len(matrix[0]) * 2 - 4
    
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            height = matrix[i][j]
            #Check visible from Left
            Left = False
            Left_check = matrix[i][:j]
            if max(Left_check) < height:
                Left = True

            #Check visible from Righ
            Right = False
            Right_check = matrix[i][j+1:]
            if max(Right_check) < height:
                Right = True

            #Check visible from Top
            Top = False
            Top_check = []
            for k in range(i):
                Top_check.append(matrix[k][j])
            if max(Top_check) < height:
                Top = True
            


            #Check visible from Bot
            Bot = False
            Bot_check = []
            for k in range(i+1,len(matrix)):
                Bot_check.append(matrix[k][j])
            if max(Bot_check) < height:
                Bot = True

            if Bot or Top or Left or Right:
                visible += 1
    return visible

def part2(matrix):
    max_score = 0

    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            height = matrix[i][j]
            
            #View Left
            Left = 0
            for k in range(j - 1, -1, -1):
                temp = matrix[i][k]
                Left += 1
                if temp >= height:
                    break
            
            #View Right
            Right = 0
            for k in range(j+1, len(matrix[i])):
                temp = matrix[i][k]
                Right += 1
                if temp >= height:
                    break

            #View Top
            Top = 0
            for k in range(i-1, -1, -1):
                temp = matrix[k][j]
                Top += 1
                if temp >= height:
                    break

            #View Bot
            Bot = 0
            for k in range(i+1, len(matrix)):
                temp = matrix[k][j]
                Bot += 1
                if temp >= height:
                    break

            score = Bot * Top * Right * Left
            if score > max_score:
                max_score = score
    return max_score


matrix = parser()
print("Part1:", part1(matrix))
print("Part2:", part2(matrix))
