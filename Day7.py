def parse():
    with open("Day7input.txt", "r") as file:
        root = {"subdirs": [], "files": [], "parrent": -1, "name": "root", "size": 0}
        current = root
        for line in file:
            line = line.strip()
            input_line = line.split(" ")

            if input_line[0] == "$":
                if input_line[1] == "cd":
                    if input_line[2] == "/":
                        current = root
                    elif input_line[2] == "..":
                        parrent = current["parrent"]
                        if parrent == -1:
                            current = root
                        else:
                            current = parrent
                    else:
                        for dick in current["subdirs"]:
                            if dick["name"] == input_line[2].strip():
                                current = dick
                                break
                        continue
                elif input_line[1] == "ls":
                    continue
            else:
                if input_line[0] == "dir":
                    current["subdirs"].append({"subdirs": [], "files": [], "parrent": current, "name": input_line[1].strip(), "size": 0})
                else:
                    current["files"].append({"size": int(input_line[0]), "name": input_line[1].strip()})
        return root

def part1_size(node):
    sume = 0
    max_s = 100000
    for dick in node["subdirs"]:
        temp = part1_size(dick)
        sume += temp
    for file in node["files"]:
        sume += file["size"]
    node["size"] = sume
    return sume

def part1_sum(node):
    temp = 0
    for dick in node["subdirs"]:
        temp += part1_sum(dick)
    if node["size"] <= 100000:
        return temp + node["size"]
    else:
        return temp

def part1(root):
    part1_size(root)
    return part1_sum(root)

def print_tree(indent, node):
    for subdir in node["subdirs"]:
        print(str(indent) + "\t" + subdir["name"] + "(dir)")
        print_tree(indent + 1, subdir)
    for file in node["files"]:
        print(str(indent) + "\t" + str(file["size"]), file["name"])

def part2_it(node, needed):
    cur = [node["name"], node["size"]]
    for subdir in node["subdirs"]:
        temp = part2_it(subdir, needed)
        if temp[1] > needed and temp[1] < cur[1]:
            cur = temp
    return cur


def part2(root):
    full = 70000000
    ava = full - root["size"]
    needed = 30000000
    delt = needed - ava

    return part2_it(root, delt)


root = parse()
print(part1(root))
print(part2(root))
#print_tree(0, root)
