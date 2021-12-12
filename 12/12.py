f = open('./input.txt', 'r')
input = f.read().splitlines()
f.close()

graph = {}
for path in input:
    key, val = path.split('-')
    if key in graph:
        graph[key].append(val)
    else:
        graph[key] = [val]
    if val in graph:
        graph[val].append(key)
    else:
        graph[val] = [key]
graph['end'] = []

small_caves = [key for key in graph.keys() if (key.islower() and key not in ('start', 'end') )]

paths = []
def DFS(graph, visited, start, end, small_caves, allow_double, doubled):
    visited.append(start)
    if start in small_caves:
        small_caves.remove(start)
    for next in graph[start]:
        if next in small_caves or next.isupper() or next == 'end':
            DFS(graph, visited.copy(), next, end, small_caves.copy(), allow_double, doubled)
        if allow_double:
            if next not in small_caves and next in reference and doubled == False:
                DFS(graph, visited.copy(), next, end, small_caves.copy(), allow_double, True)
    if start == end:
        paths.append(visited)

DFS(graph, [], 'start', 'end', small_caves, False, False)

print(f'Prva cast vysledok: {len(paths)}')

reference = [key for key in graph.keys() if (key.islower() and key not in ('start', 'end') )]
paths = []

DFS(graph, [], 'start', 'end', small_caves, True, False)

print(f'Druha cast vysledok: {len(paths)}')
