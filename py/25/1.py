data = open("i.txt").read()
lines = data.split("\n")

def parse():
    edges = []
    for line in lines:
        s, rs = line.split(": ")
        rs = rs.split(" ")
        for r in rs:
            edges.append((s, r))

    return edges

def edgesToFile(edges: list[tuple[int, int, int]]):
    with open("graph.txt", "w") as f:
        for edge in edges:
            f.write(f"{edge[0]} {edge[1]}\n")


# prints the edges to a file
edges = parse()
edgesToFile(edges)