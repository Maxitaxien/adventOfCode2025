import sys

def try_digits(bank, start, end):
    '''
    Try digits 9-1 to see if they can be applied
    '''
    # try to make best possible
    digits = reversed(list(map(lambda x: str(x), range(1, 10))))

    for digit in digits:
        for i in range(start, end): 
            if bank[i] == digit:
                return (i, digit)
    
def main():
    result = 0
    # find best of size 12
    k = 12
    while (bank := sys.stdin.readline().strip()):
        optimal_seq = ''
        # find best possible start point - must be within 12 digits of end of seq initially
        curr_start = 0
        curr_k = k
        while curr_k > 0:
            # problem:
            i, digit = try_digits(bank, curr_start, len(bank) - curr_k + 1) # type: ignore
            optimal_seq += digit
            curr_start = i + 1
            curr_k -= 1

        result += int(optimal_seq)
    
    print(result)

if __name__ == '__main__':
    main()