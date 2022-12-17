import re
import itertools

def parse():
    graph = {"start": "AA", "edges": {}, "nodes": [], "flows": {}, "opened": []}
    with open("Day16input.txt", "r") as file:
        for line in file:
            nodes = re.findall("[A-Z][A-Z]", line)
            graph["nodes"].append(nodes[0])
            graph["flows"][nodes[0]] = eval(re.findall("[0-9]+", line)[0])
            for node in nodes[1:]:
                graph["edges"].append([nodes[0], node])
        return graph

def count_flow(g):
    sum = 0
    for node in g["opened"]:
        sum += g["flows"][node]
    return sum

def dist(sn, en, g):
    queue = [[sn, 0]]
    visited = [sn]

    while len(queue) > 0:
        temp = queue.pop(0)
        for edge in g["edges"]:
            if temp[0] in edge:
                index = edge.index(temp[0])
                if en in edge:
                    return temp[1] + 1
                if edge[(index + 1) % 2] not in visited:
                    queue.append([edge[(index + 1) % 2], temp[1] + 1])
    return 1000

def find_min(g):
    start = g["start"]
    find = ["AA"]
    end = {"AA": {}}
    for node in g["nodes"]:
        if g["flows"][node] > 0 and node not in g["opened"]:
            find.append(node)
            end[node] = {}
    
    for node in find:
        skip = []
        for no in end[node]:
            skip.append(no)
        for no in find:
            if no == node or no in skip:
                continue
            temp = dist(node, no, g)
            end[node][no] = temp
            end[no][node] = temp

    return end

def simulate(g, plan, cost):
    sum = 0
    moving = 0
    start = "AA"
    target = ""
    for i in range(30):
        sum += count_flow(g)
        if moving > 0:
            moving -= 1
            continue
        if target != "" and target not in g["opened"]:
            start = target
            g["opened"].append(target)
            continue
        if len(plan) == 0:
            continue
        target = plan.pop(0)
        moving = cost[start][target] - 1
    return sum
        
def part1(g):
    cost = find_min(g)
    print(cost)
    nodes = [x for x in cost]
    nodes.remove("AA")
    permutations = itertools.permutations(nodes, len(nodes))
    high = 0
    i = 0
    for perm in permutations:
        if i % 100 == 0:
            print(i)
        g["opened"] = []
        perm = list(perm)
        temp = simulate(g, perm, cost)
        if temp > high:
            high = temp
        i += 1
    return high

g = parse()
print(part1(g))

# Either take a fast step to a node, cost 2 - opens vval
# Or take a short step, cost 1 - Doesn't open val
# Between 15 to 30 steps. ~ 2**23 computations That is not that bad.


