"""
最小全域木とはなんぞやをまずは理解済み.
クラシカル法だと、Union-Findを使うようなので、
優先度キューで書けそうなPrim法でトライ。

6 9
0 1 1
0 2 3
1 2 1
1 3 7
2 4 1
1 4 3
3 4 1
3 5 1
4 5 6
5 <-- 最小全域木の辺の重みの総和を１行に出力
"""
import heapq

def main():
    V,E = map(int,input().split())
    G = [[] for _ in range(V)]
    
    for _ in range(E):
        u,v,c = map(int,input().split())
        G[u].append((v,c))
        G[v].append((u,c))
    
    used=[0]*V
    used[0]=1
    que = [(c,u) for u,c in G[0]]
    heapq.heapify(que)

    ans = 0
    while que:
        cv,v = heapq.heappop(que)
        if used[v]:
            continue
        used[v]=1
        ans+=cv
        for k,c in G[v]:
            if used[k]:
                continue
            heapq.heappush(que,(c,k))
    print(ans)

if __name__=="__main__":
    main()
