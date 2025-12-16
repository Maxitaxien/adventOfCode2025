import sys
from collections import Counter

def find(u, uf):
    if uf[u] == u: return u
    
    parent = find(uf[u], uf)
    uf[u] = parent
    return parent

def uni(u, v, uf):
    r1 = find(u, uf)
    r2 = find(v, uf)
    uf[r1] = r2

def kruskal(uf, edges, LIM):
    amnt_seen = 0
    for (_, u, v) in edges:
        if amnt_seen >= LIM:
            return uf
        
        elif find(u, uf) != find(v, uf):
            uni(u, v, uf)
        
        amnt_seen += 1
    
    return uf

def get_dist(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2

def main():
    V = []
    #  read in input
    for line in sys.stdin:
        x, y, z = map(int, line.split(','))
        V.append((x, y, z))
    
    n = len(V)
    
    # Kruskal initiation
    uf = {}
    for i in range(n):
        uf[i] = i
    
    # Calculate distances
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            p1, p2 = V[i], V[j]
            edges.append((get_dist(p1, p2), i, j))
    
    edges = sorted(edges)

    LIM = 1000
    kruskal(uf, edges, LIM)
    
    # Find largest clusters
    k = 3
    roots = [find(i, uf) for i in range(n)]
    counts = Counter(roots)
    largest = sorted(counts.values(), reverse=True)[:k]

    mult = 1
    for x in largest:
        mult *= x
    
    print(mult)


if __name__ == '__main__':
    main()
