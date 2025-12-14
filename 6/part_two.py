import sys

def main():
    columns = {}
    lengths = {}
    for line in sys.stdin:
        new_lengths = [len(x) for x in line.split()]
        for i in range(len(new_lengths)):
            lengths[i] = max(lengths.get(i, 0), new_lengths[i])

        i = 0
        for c in line:
            column = columns.get(i, [])
            column.append(c)
            columns[i] = column
            i += 1


    # compute results
    total = 0
    i = 0
    for l in lengths.values():
        op = columns[i][-1]
        if op == '*':
            prod = 1
        for j in range(i, i + l + 1):
            col = columns[j]
            num = ''
            for val in col:
                if val.isnumeric():
                    num += val
            
            if num != '':
                if op == '+':
                    total += int(num)
                elif op == '*':
                    prod *= int(num)
        i += l + 1
        if op == '*':
            total += prod
        
    print(total)


if __name__ == '__main__':
    main()