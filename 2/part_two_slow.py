import sys

def main():
    total = 0
    ids = sys.stdin.readline().split(',')
    for id in ids:
        start, end = id.split('-')
        for i in range(int(start), int(end) + 1):
            i = str(i)

            # try different pattern lengths
            # possible lengths: 1 to half the length of the string
            for j in range(1, (len(i) // 2) + 1):
                # avoid recounting sequences:
                # iterate through in such lengths if it can divide the string cleanly
                if len(i) % j == 0:
                    chunks = [i[k:k+j] for k in range(0, len(i), j)]
                    
                    all_equal = True
                    
                    for chunk_idx in range(1, len(chunks)):
                        if chunks[chunk_idx - 1] != chunks[chunk_idx]:
                            all_equal = False
                            break

                    if all_equal:
                        total += int(i)
                        break

    print(total)

if __name__ == '__main__':
    main()
