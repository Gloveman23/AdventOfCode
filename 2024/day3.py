import re

if __name__ == "__main__":
    reg = "mul\([0-9]+,[0-9]+\)"
    reg2 = "mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)"
    file = open('input.txt')
    matches = []
    matches2 = []
    total = 0
    lines = file.readlines()
    for line in lines:
        matches += re.findall(reg, line)
        matches2 += re.findall(reg2, line)
    for match in matches:
        string = str(match).removeprefix('mul(').removesuffix(")")
        int1, int2 = string.split(',')
        int1 = int(int1)
        int2 = int(int2)
        product = int1 * int2
        total += product
        print(f"{match} = {product}")

    enabled = True
    matches3 = []
    for match in matches2:
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled:
            matches3.append(match)

    total2 = 0
    for match in matches3:
        string = str(match).removeprefix('mul(').removesuffix(")")
        int1, int2 = string.split(',')
        int1 = int(int1)
        int2 = int(int2)
        product = int1 * int2
        total2 += product
        print(f"{match} = {product}")

    print(f"Part 1: {total}")
    print(f"Part 2: {total2}")