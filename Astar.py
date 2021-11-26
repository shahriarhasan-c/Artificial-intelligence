from typing import List, Any


def aster(start, goal, g, h):
    closed_set = set([])
    open_set = {start: 0}
    came_from = {}
    g_score = {start: 0}
    f_score = {start: g_score[start] + int(h[start])}
    while len(open_set) > 0:
        current = min(open_set, key=lambda k: open_set[k])
        if current == goal:
            return recont_path(came_from, goal)
        open_set.pop(current)
        closed_set.add(current)
        for (m, weight) in get_neighbors(current):
            if m in closed_set:
                continue
            tentative_g_score = int(g_score[current]) + int(weight)
            if m not in open_set or tentative_g_score < g_score[m]:
                came_from[m] = current
                g_score[m] = tentative_g_score
                f_score[m] = int(g_score[m]) + int(h[m])
                if m not in open_set:
                    r = m
                    vl = f_score[m]
                    open_set[r] = vl
    return "failure"


def get_neighbors(v):
    if v in graph_nodes:
        return graph_nodes[v]
    else:
        return None


def recont_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path


h_dist = {}
graph_nodes = {}
f = open("E:\Codes\AI Lab\Assignment_1\input.txt", 'r')
for line in f:
    if line == '\n':
        break
    (key, val, val1) = line.split()
    tup = (val, val1)
    if key in graph_nodes:
        graph_nodes[key].append(tup)
    else:
        graph_nodes[key] = [tup]

for line in f:
    (k, v) = line.split()
    h_dist[k] = v
final = []
final = aster('A', 'J', graph_nodes, h_dist)
final.reverse()
print(final)