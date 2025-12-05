from pathlib import Path

def solve(data):

    lines = data.split("\n")

    #print(lines)

    part1 = 0
    part2 = 0

    start_num = 50
    for line in lines:
        if "R" in line:
            start_num += int(line[1:])
            start_num = start_num % 100
        else:
            start_num -= int(line[1:])
            start_num = start_num % 100
        if start_num == 0:
            part1 += 1

    start_num = 50
    for line in lines:
        if "R" in line:
            start_num += int(line[1:])
            if start_num % 100 == 0:
                part2 += (start_num // 100) - 1
            else:
                part2 += start_num // 100
            start_num = start_num % 100
        else:
            decider = start_num != 0
            start_num -= int(line[1:])
            if decider:
                if start_num < 0:
                    part2 += ((start_num // 100) * -1)
            else:
                part2 += (((start_num // 100) * -1) -1)
            start_num = start_num % 100
        if start_num == 0:
            part2 += 1

    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    start = time()
    part1, part2 = solve((Path(__file__).parent/"inputs"/"day01.txt").read_text().strip())
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")