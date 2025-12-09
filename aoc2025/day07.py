def solve(data):
    from collections import defaultdict
    lines = data.split("\n")

    part1 = 0
    part2 = 0
    
    new_lines = [lines.pop(0)]
    for i in range(len(lines)):
        if i % 2 != 0:
            new_lines.append(lines[i])
    
    next_indices = set()
    for line in new_lines:
        for i in range(len(line)):
            if line[i] == "S":
                next_indices.add(i)
                break
            if line[i] == "^" and i in next_indices:
                next_indices.remove(i)
                next_indices.add(i-1)
                next_indices.add(i+1)
                part1 += 1

    next_indices = []
    weighted_indices = defaultdict(int)
    for line in new_lines:
        removal_list = []
        append_list = []
        for i in range(len(line)):
            if line[i] == "S":
                next_indices.append(i)
                weighted_indices[i] = 1
                break
            if line[i] == "^" and i in next_indices:
                removal_list.append(i)
                append_list.append(i-1)
                append_list.append(i+1)
        for i in removal_list:
                weighted_indices[i-1] += weighted_indices[i]
                weighted_indices[i+1] += weighted_indices[i]
        for i in removal_list:
            next_indices.remove(i)
            del weighted_indices[i]
        for i in append_list:
            next_indices.append(i)
    part2 = sum(weighted_indices.values())

    graph = {}
    next_indices = set()
    j=-1
    for line in new_lines:
        i = 0
        for i in range(len(line)):
            if line[i] == "S":
                next_indices.add(i)
                break
            if line[i] == "^" and i in next_indices:
                graph[(i,j)] = [(i-1,j+1), (i+1,j+1)]
                next_indices.remove(i)
                next_indices.add(i-1)
                next_indices.add(i+1)
            i += 1
        j += 1

    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    start = time()
    part1, part2 = solve((Path(__file__).parent/"inputs"/"day07.txt").read_text().strip())
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")