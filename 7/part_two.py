import sys
from functools import lru_cache

@lru_cache(None)
def create_timelines(i, j):
    if i == n - 1:
        return 1
    
    if grid[i][j] == '^':
        total = 0
        if j - 1 >= 0:
            total += create_timelines(i + 1, j - 1)
        if j + 1 < m:
            total += create_timelines(i + 1, j + 1)
        
        return total

    else:
        return create_timelines(i + 1, j)


grid = []
for line in sys.stdin:
    grid.append(line)

first = grid[0]
start_idx = first.find('S')
n, m = len(grid), len(grid[0])

print(create_timelines(0, start_idx))