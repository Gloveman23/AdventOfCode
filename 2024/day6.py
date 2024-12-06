import copy
from tqdm import tqdm

if __name__ == "__main__":
    file = open("input.txt")
    grid = [list(line.removesuffix('\n')) for line in file.readlines()]
    grid3 = copy.deepcopy(grid)
    guard_pos = (0,0)
    guard_startpos = (0,0)
    f = False
    for i in range(len(grid)):
        if f:
            break
        for j in range(len(grid[0])):
            if grid[i][j] == '^':
                guard_pos = (i, j)
                guard_startpos = (i, j)
                f = True
                break

    guard_dirmap = {'^':(-1,0), 'v':(1,0), '<':(0,-1), '>':(0,1)}
    guard_turnmap = {'^':'>', '>':'v', 'v':'<', '<':'^'}
    while True:
        guard_dir = guard_dirmap[grid[guard_pos[0]][guard_pos[1]]]
        next_pos = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])
        if next_pos[0] < 0 or next_pos[0] >= len(grid) or next_pos[1] < 0 or next_pos[1] >= len(grid[0]):
            grid[guard_pos[0]][guard_pos[1]] = 'X'
            break
        current_obstacle = grid[next_pos[0]][next_pos[1]]
        if current_obstacle == "." or current_obstacle == 'X':
            grid[next_pos[0]][next_pos[1]] = grid[guard_pos[0]][guard_pos[1]]
            grid[guard_pos[0]][guard_pos[1]] = 'X'
            guard_pos = (next_pos[0], next_pos[1])
        elif current_obstacle == '#':
            grid[guard_pos[0]][guard_pos[1]] = guard_turnmap[grid[guard_pos[0]][guard_pos[1]]]

    count = 0
    for line in grid:
        print(''.join(line))
        count += line.count('X')
    print(f"Part 1: {count}")

    valid_obstacles = []
    tracing = {'^':'U', '>':'R', 'v':'D', '<':'L'}
    for i in tqdm(range(len(grid3))):
        for j in range(len(grid3[0])):
            if grid3[i][j] != '.':
                continue
            grid2 = copy.deepcopy(grid3)
            grid2[i][j] = 'O'
            guard_pos = guard_startpos
            while True:
                guard_dir = guard_dirmap[grid2[guard_pos[0]][guard_pos[1]]]
                next_pos = (guard_pos[0] + guard_dir[0], guard_pos[1] + guard_dir[1])
                if next_pos[0] < 0 or next_pos[0] >= len(grid2) or next_pos[1] < 0 or next_pos[1] >= len(grid2[0]):
                    break
                current_obstacle = grid2[next_pos[0]][next_pos[1]]
                if current_obstacle == '.':
                    grid2[next_pos[0]][next_pos[1]] = grid2[guard_pos[0]][guard_pos[1]]
                    grid2[guard_pos[0]][guard_pos[1]] = '.'
                    guard_pos = (next_pos[0], next_pos[1])
                elif current_obstacle in ('O', '#', 'U', 'D', 'R', 'L'):
                    new_char = tracing[grid2[guard_pos[0]][guard_pos[1]]]
                    if current_obstacle == new_char:
                        valid_obstacles += [(i, j)]
                        break
                    grid2[next_pos[0]][next_pos[1]] = new_char
                    grid2[guard_pos[0]][guard_pos[1]] = guard_turnmap[grid2[guard_pos[0]][guard_pos[1]]]

    for (a,b) in valid_obstacles:
        grid3[a][b] = 'O'
    count2 = 0
    for line in grid3:
        print(''.join(line))
        count2 += line.count('O')
    print(f"Part 2: {count2}")
