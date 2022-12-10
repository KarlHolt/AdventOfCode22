def part1():
    with open("Day10input.txt", "r") as file:
        cycle = 1
        strength = 1
        sum = 0
        record = [20, 60, 100, 140, 180, 220]
        for line in file:
            line = line.strip()
            output = line.split(" ")
            if cycle in record:
                sum += cycle * strength

            if output[0] == "noop":
                cycle += 1
            else:
                cycle += 1
                if cycle in record:
                    sum += cycle * strength
                cycle += 1
                strength += int(output[1])
        return sum

def part2():
    with open("Day10input.txt", "r") as file:
        cycle = 1
        strength = 1
        output = ["", "", "", "", "", ""]
        i = 0
        for line in file:
            if cycle > 240:
                break
            
            if len(output[i]) in [strength - 1, strength, strength + 1]:
                output[i] += "#"
            else:
                output[i] += "."
                
            if len(output[i]) == 40:
                i+=1

            line = line.strip()
            output_line = line.split(" ")

            if output_line[0] == "noop":
                cycle += 1
            else:
                cycle += 1
                if len(output[i]) in [strength - 1, strength, strength + 1]:
                    output[i] += "#"
                else:
                    output[i] += "."

                if len(output[i]) == 40:
                    i+=1
                cycle += 1
                strength += int(output_line[1])
        return output
print(part1())
out = part2()
for line in out:
    print(line)
