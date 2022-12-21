import re
import itertools

def parse():
    graph = {"start": "AA", "edges": {}, "nodes": [], "flows": {}, "opened": []}
    with open("Day16test.txt", "r") as file:
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

def dist(sn, en, g, nodes):
    queue = [[sn, 0, []]]
    visited = [sn]

    while len(queue) > 0:
        temp = queue.pop(0)
        for path in g["edges"][temp[0]]:
            if path == en:
                return [temp[1] + 1, temp[2]]
            if path not in visited:
                queue.append([path, temp[1] + 1, [temp[2], temp[2] + [path]][path in nodes]])
                visited.append(path)
    return 1000

def find_min(g):
    start = g["start"]
    find = ["AA"]
    end = {"AA": {}}
    paths = {"AA": {}}
    for node in g["nodes"]:
        if g["flows"][node] > 0 and node not in g["opened"]:
            find.append(node)
            end[node] = {}
            paths[node] = {}
    
    for node in find:
        skip = []
        for no in end[node]:
            skip.append(no)
        for no in find:
            if no == node or no in skip:
                continue
            temp = dist(node, no, g, find)
            end[node][no] = temp[0]
            end[no][node] = temp[0]
            paths[node][no] = []
            paths[no][node] = []
            
    for node in find:
        for node1 in find:
            if node1 == "AA" or node1 == node:
                continue
            for node2 in find:
                if node2 == "AA" or node2 in [node, node1]:
                    continue
                if end[node][node2] < end[node2][node1]:
                    paths[node][node1].append(node2)

    return paths, end

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
        
def average_neighbour(node, cost, g):
    neighbours = [x for x in cost if x not in g["opened"] and x != node]
    avg_neigh = {}
    for node in neighbours:
        dists = []
        for node1 in g["flows"]:
            if node == node1 or node1 in g["opened"] or g["flows"][node1] == 0:
                continue
            dists.append(g["flows"][node1] / cost[node][node1]**2)
        avg_neigh[node] = sum(dists) / len(dists)
    return avg_neigh

def insert(low, a, b):
    for i in range(len(low)):
        if low[i][0] < a and low[i][1] > b:
            temp = low[i]
            low[i] = [a,b]
            a,b = temp

def plan_routes(nodes, cost, paths, g):
    possible_routes = []
    queue = [["AA", []]]
    while len(queue) > 0:
        node, used = queue.pop(0)

        avg_neigbour = average_neighbour(node, cost, g)
        temp = max(avg_neigbour.values())
        avg = [key for key in avg_neigbour if avg_neigbour[key] == temp]

        temp = 1000
        for key in cost[node]:
            if cost[node][key] < temp and key not in g["opened"] and key not in used:
                temp = cost[node][key]
        temp1 = 0
        for key in g["flows"]:
            if g["flows"][key] > temp1 and key not in g["opened"] and key not in used:
                temp1 = g["flows"][key]
        nearest = [key for key in cost[node] if cost[node][key] == temp or g["flows"][key] == temp1]

        on_path = []
        for no in nodes:
            if no in used or no in g["opened"]:
                continue
            if no in nearest or no in avg:
                if no not in on_path:
                    on_path.append(no)
                lowest = [0, 0]
                low = [[1000, 0], [1000, 0]]
                for n in paths[node][no]:
                    if (cost[no][n] >= lowest[0] and g["flows"][n] > lowest[1]) and (cost[no][n] >= low[1][0] and avg_neigbour[n] < low[1][1]):
                        continue
                    if n not in used and n not in on_path and n not in g["opened"]:
                        if cost[no][n] < lowest[0] and g["flow"][n] > lowest[1]:
                            lowest = [cost[no][n], g["flow"][n], avg_neigbour[n]]
                        if cost[no][n] < low[1][0] and avg_neigbour[n] > low[1][1]:
                            insert(low, cost[no][n], avg_neigbour[n])
                        on_path.append(n)
        
        print("posible", len(nodes) - len(used), "choosen", len(on_path))

        continuing = False
        for no in on_path:
            continuing = True
            queue.append([no, used + [no]])
        if not continuing:
            possible_routes.append(used)
    return possible_routes

def part1(g):
    paths, cost = find_min(g)
    nodes = [x for x in cost]
    nodes.remove("AA")
    plans = plan_routes(nodes, cost, paths, g)
    high = 0
    i = 0

    for plan in plans:
        g["opened"] = []
        temp = simulate(g, plan, cost)
        if temp > high:
            print(temp, plan)
            high = temp
        i += 1
    return high

g = parse()
print(part1(g))

# Either take a fast step to a node, cost 2 - opens vval
# Or take a short step, cost 1 - Doesn't open val
# Between 15 to 30 steps. ~ 2**23 computations That is not that bad.


