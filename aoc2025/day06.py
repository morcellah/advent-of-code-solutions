def solve(data):

    lines = data.split("\n")
    for line in lines[:-1]:
        line += "   "
    lines[-1] += "  x"

    part1 = 0
    part2 = 0

    nums = []
    for line in lines[:-1]:
        nums.append(line.split())
    
    i = 0
    signs = []
    for char in lines[-1]:
        if char == "+" or char == "*":
            signs.append((char,i))
        elif char == "x":
            signs.append((char,i))
        i += 1

    for i in range(len(nums[0])):
        temp = 0
        if signs[i][0] == "+":
            for j in range(len(nums)):
                temp += int(nums[j][i])
        elif signs[i][0] == "*":
            temp = int(nums[0][i])
            for j in range(1, len(nums)):
                temp *= int(nums[j][i])
        i += 1
        part1 += temp

    for i in range(len(signs)):
        temp = 0 
        temp_num = ""
        if signs[i][0] == "+":
            k = 0
            for k in range(signs[i][1], signs[i+1][1] - 1):
                temp_num = ""
                for j in range(len(lines) - 1):
                    if lines[j][k] == " ":
                        continue
                    temp_num += lines[j][k]
                temp += int(temp_num)
        elif signs[i][0] == "*":
            for j in range(len(lines) -1):
                if lines[j][signs[i][1]] == " ":
                    continue
                temp_num += lines[j][signs[i][1]]
            temp = int(temp_num)
            for k in range(signs[i][1] +1 , signs[i+1][1] - 1):
                temp_num = ""
                for j in range(len(lines) - 1):
                    if lines[j][k] == " ":
                        continue
                    temp_num += lines[j][k]
                temp *= int(temp_num)
        part2 += temp
        if signs[i+1][0] == "x":
            break
    
    
    return part1, part2

if __name__ == "__main__":
    from pathlib import Path
    from time import time
    start = time()
    part1, part2 = solve((Path(__file__).parent/"inputs"/"day06.txt").read_text().strip())
    print(f"Part 1: {part1}\nPart 2: {part2}")
    print(f"Time Taken: {(time() - start)*1000:.2f} ms")