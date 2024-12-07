from tqdm import tqdm

def ternary(decimal):
    if decimal == 0:
        return '0'
    if decimal in cache.keys():
        return cache[decimal]
    ternary = ''
    for k in range(50, -1, -1):
        if decimal >= 2*(3**k):
            decimal -= 2*(3**k)
            ternary += '2'
        elif decimal >= (3**k):
            decimal -= (3**k)
            ternary += '1'
        else:
            if ternary != '':
                ternary += '0'
    cache[decimal] = ternary
    return ternary


cache = {0: '0'}
if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()
    rows = [line.split(':') for line in lines]
    for row in rows:
        row[0] = int(row[0])
        row[1] = row[1][1:].split(" ")
        row[-1][-1] = row[-1][-1].removesuffix('\n')
        for j in range(len(row[-1])):
            row[-1][j] = int(row[-1][j])

    total = 0
    goodrows = []
    for row in tqdm(rows):
        result = row[0]
        nums = row[1]
        operators = len(nums) - 1
        possibility = 2 ** operators
        for i in range(possibility):
            order = str(bin(i))[2:]
            order = '0'*(operators - len(order)) + order
            val = nums[0]
            for j in range(len(order)):
                if order[j] == '0':
                    val += nums[j+1]
                elif order[j] == '1':
                    val *= nums[j+1]
            if val == result:
                total += result
                goodrows.append(row)
                break

    print(f'Part 1: {total}')
    total2 = 0
    rows = [row for row in rows if row not in goodrows]
    for row in tqdm(rows):
        result = row[0]
        nums = row[1]
        operators = len(nums) - 1
        possibility = 3 ** operators
        for i in range(possibility):
            order = str(ternary(i))
            if '2' not in order:
                continue
            order = '0' * (operators - len(order)) + order
            val = nums[0]
            for j in range(len(order)):
                if order[j] == '0':
                    val += nums[j + 1]
                elif order[j] == '1':
                    val *= nums[j + 1]
                elif order[j] == '2':
                    val = int(str(val)+str(nums[j + 1]))
            if val == result:
                total2 += result
                break
    print(f'Part 2: {total2 + total}')

