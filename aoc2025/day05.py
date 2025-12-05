from pathlib import Path

def solve(data):

    lines = data.split("\n")

    #print(lines)

    part1 = 0
    part2 = 0

    ranges = []
    i = 0
    for line in lines:
        if line == "":
            break
        ranges.append(line)
        i += 1
    
    nums = []
    for line in lines[i+1:]:
        nums.append(int(line))

    for num in nums:
        for r in ranges:
            rl = r.split("-")
            if int(rl[0]) <= num <= int(rl[1]):
                part1 += 1
                break

    ranges_tuples = []
    for r in ranges:
        rl = r.split("-")
        ranges_tuples.append((int(rl[0]), int(rl[1])))

    ranges_tuples.sort()
    combined_tuples = [ranges_tuples[0]]

    i = 0
    while i < len(ranges_tuples):
        if combined_tuples[-1][1] >= ranges_tuples[i][1]:
            pass
        elif combined_tuples[-1][1] >= ranges_tuples[i][0]:
            combined_tuples[-1] = ((combined_tuples[-1][0], ranges_tuples[i][1]))
        else:
            combined_tuples.append(ranges_tuples[i])
        i += 1

    for ct in combined_tuples:
        part2 += ct[1] - ct[0] + 1

    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    start = time()
    part1, part2 = solve((Path(__file__).parent/"inputs"/"day05.txt").read_text().strip())
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")