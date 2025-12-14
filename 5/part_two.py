import sys

def main():
    fresh_ranges = []
    for line in sys.stdin:
        line = line.strip()

        if not line:
            break

        s, t = map(int, line.split('-'))
        fresh_ranges.append((s, t))

    fresh_ranges = sorted(fresh_ranges)

    # potentially combine ranges, starting from the back
    merged = []
    for s, t in fresh_ranges:
        if not merged or s > merged[-1][1] + 1:
            merged.append((s, t))
        else:
            prev_s, prev_t = merged[-1]
            merged[-1] = (prev_s, max(prev_t, t))
    
    total_fresh = 0

    for s, t in merged:
        total_fresh += t - s + 1       

    print(total_fresh)
        

if __name__ == '__main__':
    main()