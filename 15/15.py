f = open('./input.txt', 'r')
input = f.read().splitlines()
f.close()

import networkx as nx

grid = []

for row in input:
    row = list(row)
    row = [int(i) for i in row]
    grid.append(row)

SIZE = len(grid) -1

graph = nx.DiGraph()

for x in range(len(grid)):
    for y in range(len(grid)):
        if x < SIZE:
            graph.add_edge((x, y), (x + 1, y),
                                weight=grid[x + 1][y])

            graph.add_edge((x + 1, y), (x, y),
                                weight=grid[x][y])

        if y < SIZE:
            graph.add_edge((x, y), (x, y + 1),
                                weight=grid[x][y + 1])

            graph.add_edge((x, y + 1), (x, y),
                                weight=grid[x][y])

risk = 0
for node in nx.shortest_path(graph, (0,0), (SIZE,SIZE), weight='weight'):
    risk += grid[node[0]][node[1]]

risk -= grid[0][0]

print(f'Prva cast vysledok: {risk}')
