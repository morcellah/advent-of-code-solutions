from pathlib import Path

def solve(data):

    lines = data.split("\n")

    #print(lines)

    part1 = 0
    part2 = 0

    ranges = lines[0].split(",")
    for ran in ranges:
        first, last = ran.split("-")
        length = range(int(first), int(last) + 1)
        for num in length:
            num = str(num)
            if len(num) % 2 != 0:
                continue
            else:
                if num[0:int(len(num)/2)] == num[int(len(num)/2):]:
                    part1 += int(num)

    for ran in ranges:
        first, last = ran.split("-")
        length = range(int(first), int(last) + 1)
        for num in length:
            num = str(num)
            for num_parts in range(2, len(num) + 1):
                if (num[:int(len(num)/num_parts)] * num_parts) == num:
                    part2 += int(num)
                    break

    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    start = time()
    part1, part2 = solve((Path(__file__).parent/"inputs"/"day02.txt").read_text().strip())
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")

6704586098061531
85600847547