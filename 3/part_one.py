import sys

def try_digits(bank, start, end) -> tuple[int, str]:
    '''
    Try digits 9-1 to see if they can be applied
    '''
    # try to make best possible
    digits = reversed(list(map(lambda x: str(x), range(2, 10))))

    for digit in digits:
        for i in range(start, end): # no point checking the last digit for left pointer
            if bank[i] == digit:
                return (i, digit)
    
    return 0, '1'
                    

def main():
    result = 0
    while (bank := sys.stdin.readline()):
        l, left_digit = try_digits(bank, 0, len(bank) - 2)
        r, right_digit = try_digits(bank, l + 1, len(bank))
        result += int(left_digit + right_digit)
    
    print(result)




if __name__ == '__main__':
    main()