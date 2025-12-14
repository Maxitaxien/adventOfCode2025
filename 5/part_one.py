import sys

def main():
    fresh_ranges = []
    fresh_count = 0
    for line in sys.stdin:
        line = line.strip()

        if '-' in line:
            s, t = map(int, line.split('-'))
            fresh_ranges.append((s, t))
        
        elif line != '':
            num = int(line)
            for s, t in fresh_ranges:
                if s <= num <= t:
                    fresh_count += 1
                    break
        
    
    print(fresh_count)
        

if __name__ == '__main__':
    main()