from collections import deque

data = open("i.txt").read()
lines = data.split("\n")

def parse():
    edges = set()
    for line in lines:
        s, rs = line.split(": ")
        rs = rs.split(" ")
        for r in rs:
            edges.add((s, r))

    return edges

# only two groups => count one of them
def bfs(edges: set[tuple[str, str]]):
    adj: dict[str, set[str]] = dict()
    for edge in edges:
        if not edge[0] in adj:
            adj[edge[0]] = set()
        adj[edge[0]].add(edge[1])

    visited = set()
    q = deque()
    q.append([e for e in edges][0][0])
    while q:
        n = q.popleft()
        for node in adj[n]:
            if node in visited: continue
            visited.add(node)
            q.append(node)

    return len(visited), len(adj.keys()) - len(visited)

def edgesToFile(edges: list[tuple[int, int, int]]):
    with open("graph.txt", "w") as f:
        for edge in edges:
            f.write(f"{edge[0]} {edge[1]}\n")

def solve():
    edges = parse()
    # remove connections you got from analyzing the graph
    #toDelete = [("hfx", "pzl"), ("bvb", "cmg"), ("nvd", "jqt")]
    toDelete = [("vkb", "jzj"), ("vrx", "hhx"), ("grh", "nvh")]
    for e in edges.copy():
        edges.add((e[1], e[0]))

    for e in toDelete:
        edges.remove(e)
        edges.remove((e[1], e[0]))

    edgesToFile(edges)

    count, count2 = bfs(edges)

    return count, count2, count * count2

print(solve())