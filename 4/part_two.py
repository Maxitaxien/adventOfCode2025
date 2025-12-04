import sys
# we still want the grid of counts
# but now we can remove as we go and then keep trying
# what would definitely work is just updating the counts after we remove
# maybe not the most efficient but can be a first step

# improvement would be to instead of scanning the grid, have all indexes in a queue
# push all neighbours into the queue to be rechecked after we remove a '@'

add = lambda x: x + 1
subtract = lambda x: x - 1

def update_surrounding(f, grid: list[list[int]], counts: list[list[int]], i: int, j: int):
    n = len(grid)
    m = len(grid[0])
    directions = [(1, 1), (1, 0), (0, 1), (0, -1), (-1, 0), (1, -1), (-1, 1), (-1, -1)]

    for (delta_i, delta_j) in directions:
        if 0 <= i + delta_i < n and 0 <= j + delta_j < m:
            counts[i + delta_i][j + delta_j] = f(counts[i + delta_i][j + delta_j])
    
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
                counts = update_surrounding(add, grid, counts, i, j)
    
    # go through counts
    picked = set()
    pickable = 0
    i, j = 0, 0
    while i < n and j < m:
        if grid[i][j] == '@' and counts[i][j] < 4 and (i, j) not in picked:
            pickable += 1
            picked.add((i, j))
            counts = update_surrounding(subtract, grid, counts, i, j)
            i, j = 0, 0 # reset
        else:
            if j < m - 1:
                j += 1
            elif i < n:
                i += 1
                j = 0
    
    print(pickable)




if __name__ == '__main__':
    main()