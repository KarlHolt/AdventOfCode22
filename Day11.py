import math
import copy

def parser():
    with open("Day11input.txt", "r") as file:
        monkeys = []
        for line in file:
            line = line.strip()
            out = line.split(" ")
            if len(out) == 1:
                continue
            if out[0] == "Monkey":
                monkeys.append({"items": [], "op": "", "test": 0, "trans": [], "val": 0})
            elif out[0] == "Starting":
                for i in range(2, len(out)):
                    monkeys[-1]["items"].append(int(out[i].replace(",", "")))
            elif out[0] == "Operation:":
                if out[-1] == "old":
                    monkeys[-1]["op"] = lambda x: x * x
                else:
                    monkeys[-1]["val"] = int(out[-1])
                    if out[-2] == "+":
                        monkeys[-1]["op"] = "add"
                    elif out[-2] == "*":
                        monkeys[-1]["op"] = "multi"
            elif out[0] == "Test:":
                monkeys[-1]["test"] = int(out[-1])
            elif out[1] in ["true:", "false:"]:
                monkeys[-1]["trans"].insert(0, int(out[-1]))
        return monkeys

def part1(monkeys):
    counter = [0] * len(monkeys)
    for j in range(10000):
        for i in range(len(monkeys)):
            for item in monkeys[i]["items"]:
                counter[i] += 1
                
                if monkeys[i]["op"] == "add":
                    val1 = monkeys[i]["val"] + item
                elif monkeys[i]["op"] == "multi":
                    val1 = monkeys[i]["val"] * item
                else:
                    val1 = item * item

                k = 11 * 5 * 7 * 2 * 17 * 13 * 3 * 19
                
                val = val1 % k

                receiver_monkey = monkeys[i]["trans"][val % monkeys[i]["test"] == 0]

                monkeys[receiver_monkey]["items"].append(val)
            monkeys[i]["items"] = []
    max = maks = counter[0]
    print(counter)
    for i in range(1, len(counter)):
        if counter[i] > maks:
            max = maks
            maks = counter[i]
        elif counter[i] > max:
            max = counter[i]
    return max * maks

m = parser()
print(part1(m))
