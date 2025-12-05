from pathlib import Path

def solve(data):

    lines = data.split("\n")

    #print(lines)

    part1 = 0
    part2 = 0


    #for line in lines:
    #   nums = list(line)
    #    int_nums = [int(s) for s in nums]
    #    largest_combo = 0
    #    for i in range(len(int_nums)):
    #        for j in range(i + 1, len(int_nums)):
    #            if int(str(int_nums[i]) + str(int_nums[j])) > largest_combo:
    #                largest_combo = int(str(int_nums[i]) + str(int_nums[j]))
    #    part1 += largest_combo

    def max_joltage(line, jolt_len):
        answer = 0
        nums = list(line)
        int_nums = [int(s) for s in nums]
        to_return = ""
        i = 0
        nums_needed = jolt_len
        while i < len(int_nums):
            temp = max(int_nums[i: len(int_nums) - nums_needed + 1])
            i += int_nums[i: len(int_nums) - nums_needed + 1].index(temp) + 1
            to_return += str(temp)
            nums_needed -= 1
            if nums_needed == 0:
                break
        answer += int(to_return)
        return answer

    for line in lines:

        part1 += max_joltage(line, 2)
        part2 += max_joltage(line, 12)

    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    start = time()
    part1, part2 = solve((Path(__file__).parent/"inputs"/"day03.txt").read_text().strip())
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")