def solution(x):
    with open("Day6input.txt", "r") as file:
        buffer = []
        for line in file:
            for char in line:
                buffer.append(char)
                if len(buffer) > x:
                    if len(set(buffer[-x:])) == x:
                        return len(buffer)

print("part1:", solution(4))
print("part2:", solution(14))
