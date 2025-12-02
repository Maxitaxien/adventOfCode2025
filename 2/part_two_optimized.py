import sys

def main():
    total = 0
    ids = sys.stdin.readline().split(',')
    for id in ids:
        start, end = id.split('-')
        for i in range(int(start), int(end) + 1):
            i = str(i)

            if i in (i + i)[1:-1]:
                total += int(i)


    print(total)

if __name__ == '__main__':
    main()
