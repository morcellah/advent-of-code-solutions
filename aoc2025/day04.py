from pathlib import Path

def solve(data):

    lines = list(map(list, data.split("\n")))

    #print(lines)

    part1 = 0
    global part2
    part2 = 0

    # for line in lines:
    #     for i, char in enumerate(line):
    #         num_surrounding = 0
    #         if line[i] == "@":
    #             if j >= 0:
    #                 if i - 1 >= 0:
    #                     if lines[j][i-1] == "@":
    #                         num_surrounding += 1
    #                 if lines[j][i] == "@":
    #                     num_surrounding += 1
    #                 if i + 1 < len(line):
    #                     if lines[j][i+1]:
    #                         num_surrounding += 1
    #             if i - 1 >= 0:
    #                 if lines[j+1][i-1] == "@":
    #                     num_surrounding += 1
    #             if i + 1 < len(line):
    #                 if lines[j+1][i+1] == "@":
    #                     num_surrounding += 1
    #             if j + 2 < len(lines):
    #                 if i - 1 >= 0:
    #                     if lines[j+2][i-1] == "@":
    #                         num_surrounding += 1
    #                 if lines[j+2][i] == "@":
    #                     num_surrounding += 1
    #                 if i + 1 < len(line):
    #                     if lines[j+2][i+1] == "@":
    #                         num_surrounding += 1
    #         if num_surrounding < 4:
    #             part1 += 1
    #     j += 1

    def valid_pos(i, j):
        return 0 <= i < len(lines[0]) and 0 <= j < len(lines)

    for i in range(len(lines[0])):
        for j in range(len(lines)):
            num_surrounding = 0
            if lines[j][i] != "@":
                continue
            for i2 in [i - 1, i, i + 1]:
                for j2 in [j-1, j, j+1]:
                    if valid_pos(i2, j2) and (i2 != i or j2 != j) and lines[j2][i2] == "@":
                        num_surrounding += 1
            part1 += 1 if num_surrounding < 4 else 0
    
    def remove_roles(if_changed):
        global part2
        while if_changed:
            if_changed = False
            for i in range(len(lines[0])):
                for j in range(len(lines)):
                    num_surrounding = 0
                    if lines[j][i] != "@":
                        continue
                    for i2 in [i - 1, i, i + 1]:
                        for j2 in [j-1, j, j+1]:
                            if valid_pos(i2, j2) and (i2 != i or j2 != j) and lines[j2][i2] == "@":
                                num_surrounding += 1
                    if num_surrounding < 4:
                        part2 += 1
                        lines[j][i] = "x"
                        if_changed = True
        if not if_changed:
            return
        remove_roles(if_changed)

    remove_roles(True)

    return part1, part2


if __name__ == "__main__":
    from pathlib import Path
    from time import time
    start = time()
    part1, part2 = solve((Path(__file__).parent/"inputs"/"day04.txt").read_text().strip())
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")