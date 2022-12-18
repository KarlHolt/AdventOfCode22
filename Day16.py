import re
import itertools

def parse():
    graph = {"start": "AA", "edges": {}, "nodes": [], "flows": {}, "opened": []}
    with open("Day16input.txt", "r") as file:
        for line in file:
            nodes = re.findall("[A-Z][A-Z]", line)
            graph["nodes"].append(nodes[0])
            graph["flows"][nodes[0]] = eval(re.findall("[0-9]+", line)[0])
            graph["edges"][nodes[0]] = []
            for node in nodes[1:]:
                graph["edges"][nodes[0]].append(node)
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
        for path in g["edges"][temp[0]]:
            if path == en:
                return temp[1] + 1
            if path not in visited:
                queue.append([path, temp[1] + 1])
                visited.append(path)
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
    start = "AA"
    left = 30
    t_flow = 0
    for t in plan:
        flow = count_flow(g)
        consumed_time = cost[start][t]
        start = t
        if left < consumed_time + 1:
            break
        left -= (consumed_time + 1)
        t_flow += flow * (consumed_time + 1)
        g["opened"].append(t)
    flow = count_flow(g)
    return t_flow + left * flow
        
def part1(g):
    cost = find_min(g)
    nodes = [x for x in cost]
    nodes.remove("AA")
    permutations = itertools.permutations(nodes, len(nodes))
    high = 0
    i = 0
    for perm in permutations:
        g["opened"] = []
        perm = list(perm)
        temp = simulate(g, perm, cost)
        if temp > high:
            print(temp)
            high = temp
        i += 1
    return high

g = parse()
print(part1(g))

# Either take a fast step to a node, cost 2 - opens vval
# Or take a short step, cost 1 - Doesn't open val
# Between 15 to 30 steps. ~ 2**23 computations That is not that bad.


