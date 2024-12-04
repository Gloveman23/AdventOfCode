def count_xmas(words, words2, x, y):
    count = 0
    for dy in range(-1,2):
        for dx in range(-1,2):
            if dy == 0 and dx == 0:
                continue
            M_POS = (x+dx, y+dy)
            A_POS = (x+2*dx, y+2*dy)
            S_POS = (x+3*dx, y+3*dy)
            if S_POS[0] > len(words[0]) or S_POS[1] > len(words) or S_POS[0] < 0 or S_POS[1] < 0:
                continue
            try:
                M, A, S = [words[a][b] for (b,a) in (M_POS, A_POS, S_POS)]
                if M == "M" and A == "A" and S == "S":
                    words2[y][x].append([dx, dy])
                    count += 1
            except:
                ...
    return count


def count_x_mas(words, x, y):
    if x == 0 or y == 0 or x == len(words[0])-1 or y == len(words)-1:
        return 0
    letters = [
        words[y-1][x-1],
        words[y+1][x-1],
        words[y-1][x+1],
        words[y+1][x+1]
    ]
    if letters[0] != letters[3] and sorted(letters) == sorted(["M","M","S","S"]):
        return 1
    return 0


if __name__ == "__main__":
    file = open("input.txt")
    lines = file.readlines()
    grid = [[line[i] for i in range(len(line)-1)] for line in lines]
    words2 = [[[] for _ in word] for word in grid]
    total2 = 0
    total = 0
    words3 = [[line[i] for i in range(len(line)-1)] for line in lines]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            letter = grid[i][j]
            if letter == 'X':
                words3[i][j] = '.'
                total += count_xmas(grid,words2,j,i)
            elif letter == 'A':
                total2 += (b := count_x_mas(grid,j,i))
                if b == 0:
                    words3[i][j] = '.'
            else:
                words3[i][j] = '.'
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            letter = words3[i][j]
            if letter == "A":
                words3[i-1][j-1] = grid[i-1][j-1]
                words3[i + 1][j + 1] = grid[i + 1][j + 1]
                words3[i + 1][j - 1] = grid[i + 1][j - 1]
                words3[i - 1][j + 1] = grid[i - 1][j + 1]
    for i in range(len(grid)):
        tops = []
        middles = []
        bottoms = []
        for j in range(len(grid[0])):
            letter = grid[i][j]
            if letter != 'X':
                top = "   "
                bottom = top
                mittel = " "+letter+" "
                tops.append(top)
                bottoms.append(bottom)
                middles.append(mittel)
            else:
                tm = "^" if [0, -1] in words2[i][j] else " "
                tr = "7" if [1, -1] in words2[i][j] else " "
                tl = "F" if [-1, -1] in words2[i][j] else " "
                bm = "v" if [0, 1] in words2[i][j] else " "
                bl = "L" if [-1, 1] in words2[i][j] else " "
                br = "J" if [1, 1] in words2[i][j] else " "
                ml = "<" if [-1, 0] in words2[i][j] else " "
                mr = ">" if [1, 0] in words2[i][j] else " "
                top = tl + tm + tr
                bottom = bl + bm + br
                mittel = ml + letter + mr
                tops.append(top)
                bottoms.append(bottom)
                middles.append(mittel)
        print("".join(tops) + '\n' + "".join(middles)+ '\n' + "".join(bottoms))
    print(f"Part 1: {total}")
    print('\n'.join([''.join(word) for word in words3]))
    print(f"Part 2: {total2}")