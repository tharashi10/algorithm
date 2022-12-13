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
- Template
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

## DP

