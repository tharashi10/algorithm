## Graph Data Structure
- A graph G is represented as `G(V,E)` .
- Basically we use Adjacency Matirix.
  - however, space required `O(v^2)`
  - using linked List is better `O(V+E)`
- Graph search
  - BFS
  - DFS
  - Is BFS always preferrable??
    - For Large graphs, DFS is hugely more efficient.
  - Dijskstra’s Short Path 
    - like BFS
    - Using cost dictionary cost {} in py
- BFS Template
```py
def bfs(x):
    while len(que)!=0:
        vid = que.pop(0)
        if vid==x:
            break
        for v in A[vid]:
            if dist[v]!=-1:
                continue
            dist[v]=(dist[vid]+1)
            que.append(v)
```
- Dijskstra Template
```py
import heapq
def dijkstra(s):
    hq = [(0,s)] # (Weight,node), tuple
    while hq:
        cst, now = heapq.heappop(hq)
        for next in G[now]:
            tmp = cst + cost[(now,next)]
            if tmp < dist[next]:
                dist[next] = tmp
                heapq.heappush(hq,(tmp,next))
    return dist 
```

## DP

