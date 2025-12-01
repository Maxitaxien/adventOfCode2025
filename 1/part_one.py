import sys

def main():
    curr = 50
    amnt_zeroes = 0
    while (line := sys.stdin.readline()):
        direction = line[0]
        amnt = int(line[1:])
        if direction == "L": curr -= amnt
        else: curr += amnt

        curr = curr % 100

        if curr == 0: amnt_zeroes += 1
    
    print(amnt_zeroes)

if __name__ == '__main__':
    main()