import networkx as nx

f = open('./input.txt', 'r')
input = f.read().splitlines()
f.close()

grid = []

for row in input:
    row = list(row)
    row = [int(i) for i in row]
    grid.append(row)

def find_risk(grid):
    size = len(grid) -1

    graph = nx.DiGraph()

    for x in range(len(grid)):
        for y in range(len(grid)):
            if x < size:
                graph.add_edge((x, y), (x + 1, y),
                                    weight=grid[x + 1][y])

                graph.add_edge((x + 1, y), (x, y),
                                    weight=grid[x][y])

            if y < size:
                graph.add_edge((x, y), (x, y + 1),
                                    weight=grid[x][y + 1])

                graph.add_edge((x, y + 1), (x, y),
                                    weight=grid[x][y])

    risk = 0
    for node in nx.shortest_path(graph, (0,0), (size,size), weight='weight'):
        risk += grid[node[0]][node[1]]

    risk -= grid[0][0]
    return risk

risk = find_risk(grid)

print(f'Prva cast vysledok: {risk}')

new_grid = []
for g in range(0,5):
    for j in range(len(grid)):
        new_row = []
        for i in range(0,5):
            for item in grid[j]:
                new_item = item + i + g
                if new_item > 9:
                    new_item = new_item % 9
                new_row.append(new_item)
        new_grid.append(new_row)

risk = find_risk(new_grid)

print(f'Druha cast vysledok: {risk}')
