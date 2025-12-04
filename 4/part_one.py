import sys
# IDEA: Keep a grid of counts.
# Iterate over grid. On each spot, update the eight surrounding counts if it is '@' else do nothing
# Iterate over final grid again at the end. Keep a count of '@' with fewer than 4 neighbours.

def update_surrounding(grid: list[list[int]], counts: list[list[int]], i: int, j: int):
    n = len(grid)
    m = len(grid[0])
    directions = [(1, 1), (1, 0), (0, 1), (0, -1), (-1, 0), (1, -1), (-1, 1), (-1, -1)]

    for (delta_i, delta_j) in directions:
        if 0 <= i + delta_i < n and 0 <= j + delta_j < m:
            counts[i + delta_i][j + delta_j] += 1
    
    return counts

def main():
    # READ GRID:
    grid = []
    while (line := sys.stdin.readline().strip()):
        grid.append(line)

    n = len(grid)
    m = len(grid[0])

    counts = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '@':
                counts = update_surrounding(grid, counts, i, j)
    
    # go through counts
    pickable = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '@' and counts[i][j] < 4:
                pickable += 1
    
    print(pickable)




if __name__ == '__main__':
    main()