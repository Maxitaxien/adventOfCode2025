import sys


first = sys.stdin.readline()
indexes = {first.find('S')}


splits = 0

for line in sys.stdin:
    for i in range(len(line)):
        if line[i] == '^' and i in indexes:
            splits += 1
            indexes = indexes - {i}
            indexes.add(i - 1)
            indexes.add(i + 1)

print(splits)