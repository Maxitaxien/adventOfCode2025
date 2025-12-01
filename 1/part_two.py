import sys

def main():
    curr = 50
    amnt_zeroes = 0
    while (line := sys.stdin.readline()):
        direction = line[0]
        amnt = int(line[1:])

        if direction == "L": 
            new = curr - amnt
            amnt_times = (curr - 1) // 100 - (new - 1) // 100 # offset by one to avoid counting bug
            amnt_zeroes += amnt_times 
        else: 
            new = curr + amnt
            amnt_times = new // 100 - curr // 100
            amnt_zeroes += amnt_times 

        curr = new % 100

    print(amnt_zeroes)

if __name__ == '__main__':
    main()