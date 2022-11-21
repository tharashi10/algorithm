"""

Input()
4 5 0
0 1 1
0 2 4
1 2 2
2 3 1
1 3 5
---
0
1
3
4
"""
import heapq

def dijkstra(s):
    cost = [float('inf')]*V
    cost[s] = 0
    
    hq = [(0,s)]
    heapq.heapify(hq)

    while hq:
        cst,v = heapq.heappop(hq)
        if cost[v] < cst:
            continue
        for d,u in G[v]:
            tmp = d + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                heapq.heappush(hq,(tmp,u))
    return cost

if __name__ == '__main__':
    V,E,r = map(int,input().split())
    G = [[] for _ in range(V)]
    for i in range(E):
        s,t,d = map(int,input().split())
        G[s].append((d,t))  # [[(1, 1), (2, 4)], [(2, 2), (3, 5)], [(3, 1)]]
    
    ans = dijkstra(0)
    for k in range(len(ans)):
        print(ans[k])
