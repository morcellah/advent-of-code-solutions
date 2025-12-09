def solve(data):
    from collections import defaultdict

    lines = data.split("\n")

    part1 = 0
    part2 = 0

    def distance(p1,p2):
        x1 = p1[0]
        y1 = p1[1]
        z1 = p1[2]
        x2 = p2[0]
        y2 = p2[1]
        z2 = p2[2]
        return ((int(x1)-int(x2))**2 + (int(y1)-int(y2))**2 + (int(z1)-int(z2))**2) **(1/2)

    def all_connections(list_of_coords, connected):
        to_return = []
        for i in range(len(list_of_coords)):
            for j in range(i+1, len(list_of_coords)):
                if (i,j) in connected:
                    continue
                dist = distance(list_of_coords[i], list_of_coords[j])
                to_return.append((dist,i,j))
        return to_return
    
    list_of_coords_tuples = []
    for line in lines:
        list_of_coords_tuples.append(tuple(line.split(",")))
    
    distance_tuples = []
    indice_tuple = all_connections(list_of_coords_tuples,distance_tuples)
    distance_tuples.append((indice_tuple))

    sorted_distance_tuples = sorted(distance_tuples[0])
    connected = sorted_distance_tuples[:1000]
    
    connected_graph = defaultdict(set)
    for _,i,j in connected:
        connected_graph[i].add(j)
        connected_graph[j].add(i)

    visited = set()
    def make_paths(cg, key):
        visited.add(key)
        temp_size = 1
        for value in connected_graph[key]:
            if value in visited:
                continue
            visited.add(value)
            temp_size += make_paths(cg, value)
        return temp_size
    
    def bfs(start,adjs,seen):
        q = [start]
        size = 0
        seen.add(start)
        while q:
            current = q.pop(0)
            size += 1
            for adj in adjs[current]:
                if adj in seen:
                    continue
                seen.add(adj)
                q.append(adj)
        return size

    sizes = []
    seen = set()
    for point in connected_graph.keys():
        if point not in visited:
            sizes.append(make_paths(connected_graph,point))

    from math import prod
    part1 = prod(sorted(sizes,reverse=True)[:3])
   
    i=0
    connections = 0
    connected_list = set()
    while len(connected_list) < len(lines):
        if sorted_distance_tuples[i][1] in connected_list and sorted_distance_tuples[i][2] in connected_list:
            i += 1
        else:
            connected_list.add(sorted_distance_tuples[i][1])
            connected_list.add(sorted_distance_tuples[i][2])
            connections += 1
    first_index = sorted_distance_tuples[i][1]
    second_index = sorted_distance_tuples[i][2]
    part2 = int(list_of_coords_tuples[first_index][0]) * int(list_of_coords_tuples[second_index][0])

    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    start = time()
    part1, part2 = solve((Path(__file__).parent/"inputs"/"day08.txt").read_text().strip())
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")