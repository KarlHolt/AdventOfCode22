import re
import itertools
import math

def parse(filename):
    graph = {"start": "AA", "edges": {}, "nodes": [], "flows": {}, "opened": []}
    with open(filename, "r") as file:
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

def insert(candidates, value, node):
    c_node = [node, value]
    for i in range(len(candidates)):
        if candidates[i][1] < c_node[1]:
            temp = candidates[i]
            candidates[i] = c_node
            c_node = temp

def find_routes(nodes, g, cost):
    queue = [["AA", 30, []]]
    candidates = []
    while len(queue) > 0:
        current = queue.pop(0)
        neigbours = []
        neigbours_pon = {}
        neigbours_neigbours_pon = {}

        for node in nodes:
            if node in current[2]:
                continue
            neigbours.append(node)
            time_left = current[1] - cost[current[0]][node] - 1
            if time_left < 0:
                time_left = 0
            neigbours_pon[node] = time_left * g["flows"][node]
            neigbours_neigbours_pon[node] = 0
            for mode in nodes:
                if mode in current[2] or node == mode:
                    continue
                time_left = current[1] - cost[node][mode] - 1 - cost[current[0]][node]
                if time_left < 0:
                    time_left = 0
                neigbours_neigbours_pon[node] += time_left * g["flows"][node]
        
        cand_neigbours = []
        length = math.ceil(math.sqrt(len(neigbours))*3) 
        cands = []
        for i in range(length):
            cands.append(["", 0])
        for node in neigbours_pon:
            temp = neigbours_pon[node] + neigbours_neigbours_pon[node]
            insert(cands, temp, node)
        for c in cands:
            if c[0] != "":
                cand_neigbours.append(c[0]) 

        if len(cand_neigbours) == 0:
            candidates.append(current[2])

        for candidate in cand_neigbours:
            queue.append([candidate, current[1] - cost[current[0]][candidate] - 1, current[2] + [candidate]])
    return candidates

def part1(g):
    cost = find_min(g)
    nodes = [x for x in cost]
    nodes.remove("AA")
    plans = find_routes(nodes, g, cost)
    high = 0
    for plan in plans:
        g["opened"] = []
        temp = simulate(g, plan, cost)
        if temp > high:
            #print(temp, plan)
            high = temp
    return high

def find_routes2(nodes, g, cost):
    queue = [[["AA", "AA"], [26, 26], [[], []]]]
    candidates = []
    while len(queue) > 0:
        current = queue.pop(0)
        neigbours = [[], []]
        neigbours_pon = [{}, {}]
        neigbours_neigbours_pon = [{}, {}]

        for node in nodes:
            if node in current[2][0] or node in current[2][1]:
                continue
            neigbours[0].append(node)
            neigbours[1].append(node)
            time_left = [0,0]
            time_left[0] = current[1][0] - cost[current[0][0]][node] - 1
            time_left[1] = current[1][1] - cost[current[0][1]][node] - 1
            if time_left[0] < 0:
                time_left[0] = 0
            if time_left[1] < 0:
                time_left[1] = 0
            neigbours_pon[0][node] = time_left[0] * g["flows"][node]
            neigbours_pon[1][node] = time_left[1] * g["flows"][node]

            neigbours_neigbours_pon[0][node] = 0
            neigbours_neigbours_pon[1][node] = 0
            for mode in nodes:
                if mode in current[2][0] or mode in current[2][1] or node == mode:
                    continue
                time_left[0] = current[1][0] - cost[node][mode] - 1 - cost[current[0][0]][node]
                time_left[1] = current[1][1] - cost[node][mode] - 1 - cost[current[0][1]][node]
                if time_left[0] < 0:
                    time_left[0] = 0
                if time_left[1] < 0:
                    time_left[1] = 0
                neigbours_neigbours_pon[0][node] += time_left[0] * g["flows"][mode]
                neigbours_neigbours_pon[1][node] += time_left[1] * g["flows"][mode]
        
        cand_neigbours = [[], []]
        length = max(math.ceil(math.sqrt(len(neigbours))), 3)
        cands = [[], []]
        for i in range(length):
            cands[0].append(["", 0])
            cands[1].append(["", 0])
        for node in neigbours_pon[0]:
            temp = neigbours_pon[0][node] + neigbours_neigbours_pon[0][node]
            temp1 = neigbours_pon[1][node] + neigbours_neigbours_pon[1][node]
            
            insert(cands[0], temp, node)
            insert(cands[1], temp1, node)
        for i in range(len(cands[0])):
            if cands[0][i][0] != "":
                cand_neigbours[0].append(cands[0][i][0])
            if cands[1][i][0] != "":
                cand_neigbours[1].append(cands[1][i][0])

        if len(cand_neigbours[1]) == 0:
            candidates.append(current[2])

        if len(cand_neigbours[1]) == 0 and len(cand_neigbours[0]) > 0:
            for candidate in cand_neigbours[0]:
                queue.append([
                    [candidate, current[0][1]],
                    [current[1][0] - cost[current[0][0]][candidate] - 1, 
                     current[1][1]],
                    [current[2][0] + [candidate], current[2][1]]])
        if len(cand_neigbours[0]) == 0 and len(cand_neigbours[1]) > 0:
            for candidate in cand_neigbours[1]:
                queue.append([
                    [current[0][0], candidate],
                    [current[1][0],
                     current[1][1] - cost[current[0][1]][candidate] - 1],
                    [current[2][0], current[2][1] + [candidate]]])

        for candidate in cand_neigbours[0]:
            for candi in cand_neigbours[1]:
                if candi == candidate:
                    continue
                queue.append([
                    [candidate, candi], 
                    [current[1][0] - cost[current[0][0]][candidate] - 1, 
                     current[1][1] - cost[current[0][1]][candi] - 1], 
                    [current[2][0] + [candidate], current[2][1] + [candi]]])
    return candidates

def simulate2(g, plan, cost):
    start = ["AA", "AA"]
    left = 26
    t_flow = 0
    c_moving = [0, 0]
    i = j = 0
    while left > 0:
        t_flow += count_flow(g)
        if c_moving[0] == 0 and i < len(plan[0]):
            temp = plan[0][i]
            c_moving[0] = cost[start[0]][temp] + 1
            start[0] = temp
            i+=1
        if c_moving[1] == 0 and j < len(plan[1]):
            temp = plan[1][j]
            c_moving[1] = cost[start[1]][temp] + 1
            start[1] = temp
            j+=1
        
        c_moving[1] -= 1
        c_moving[0] -= 1

        if c_moving[0] == 0:
            g["opened"].append(start[0])
        if c_moving[1] == 0:
            g["opened"].append(start[1])
        left -= 1
    return t_flow


def part2(g):
    cost = find_min(g)
    nodes = [x for x in cost]
    nodes.remove("AA")
    plans = find_routes2(nodes, g, cost)
    high = 0
    for plan in plans:
        g["opened"] = []
        temp = simulate2(g, plan, cost)
        if temp > high:
#            print(temp, plan)
            high = temp
    return high


def test():
    solution = [1651, 2640, 13468, 1288, 2400]
    for i in range(5):
        g = parse("Day16test" + str(i + 1) + ".txt")
        temp = part1(g)
        if temp == solution[i]:
            print("Solution to test", i, "is correct")
        else:
            print("Failed test", i, "Your guess =", temp, "correct answer:", solution[i])

def real():
    g = parse("Day16input.txt")
    print("part1:", part1(g))
    g = parse("Day16input.txt")
    print("part2:", part2(g))

def test2():
    solution = [1707, 2670, 12887, 1484, 3680]
    for i in range(5):
        g = parse("Day16test" + str(i + 1) + ".txt")
        temp = part2(g)
        if temp == solution[i]:
            print("Solution to test", i, "is correct")
        else:
            print("Failed test", i, "Your guess =", temp, "correct answer:", solution[i])

#test2()
real()

# Either take a fast step to a node, cost 2 - opens vval
# Or take a short step, cost 1 - Doesn't open val
# Between 15 to 30 steps. ~ 2**23 computations That is not that bad.


