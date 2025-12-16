import sys

def find(u, uf):
    if uf[u] == u: return u
    
    parent = find(uf[u], uf)
    uf[u] = parent
    return parent

def uni(u, v, uf):
    r1 = find(u, uf)
    r2 = find(v, uf)
    uf[r1] = r2

def kruskal(uf, V, edges, n):
    amnt_merged = 0
    for (_, u, v) in edges:
        if find(u, uf) != find(v, uf):
            uni(u, v, uf)
            if amnt_merged == n - 2: # final merge! record x-products
                x1, x2 = V[u][0], V[v][0]
                return x1 * x2
            
            amnt_merged += 1
        
    return -1

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

    result = kruskal(uf, V, edges, n)
    print(result)


if __name__ == '__main__':
    main()
