import sys

def main():
    total = 0
    ids = sys.stdin.readline().split(',')
    for id in ids:
        start, end = id.split('-')
        for i in range(int(start), int(end) + 1):
            i = str(i)
            if len(i) % 2 == 0:
                mid = len(i) // 2
                if i[:mid] == i[mid:]: # invalid
                    total += int(i)

    print(total)


if __name__ == '__main__':
    main()
