import sys

def add_line(grid, line):
    for i in range(len(line)):
        elem = line[i].strip()
        if elem:
            num = int(elem)
            grid[i].append(num)
    
    return grid

def main():
    first_line = sys.stdin.readline().split()
    m = len(first_line)
    grid = [[] for _ in range(m)]
    grid = add_line(grid, first_line)


    for line in sys.stdin:
        line = line.strip().split()

        if line[0].isnumeric():
            add_line(grid, line)
        else:
            operations = line
    
    total = 0
    for j in range(len(operations)):
        col = grid[j]
        if operations[j] == '+':
            total += sum(col)
        else:
            mult = 1
            for num in col:
                mult *= num
            
            total += mult
    print(total)

if __name__ == '__main__':
    main()