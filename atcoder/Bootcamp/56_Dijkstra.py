"""
単一最短経路
記事見たけど、普通にTLEするものが多い.
以下の記事は有用.
https://note.com/omotiti/n/n161899ff99b6

3つ用意する
・cost {}: (from,to):distance の辞書マスタ <-- 2d arrayでやるとTLEになる
・dist []: 累積の距離 初期値は全て INF
・hq = [tuple()] : tuple(tmp_dist,node)

---
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
    hq = [(0,s)]
    while hq:
        cst, now = heapq.heappop(hq)
        for next in G[now]:
            tmp = cst + cost[(now,next)]
            if tmp < dist[next]:
                dist[next] = tmp
                heapq.heappush(hq,(tmp,next))
    return dist

if __name__ == '__main__':
    V,E,r = map(int,input().split())
    G = [[] for _ in range(V)]
    INF = 10**10
    cost = {}
    dist = [INF]*V
    dist[r]=0

    for i in range(E):
        s,t,d = map(int,input().split())
        G[s].append(t)
        cost[(s,t)]=d
    
    ans = dijkstra(r)
    for i in range(V):
        if ans[i]==INF:
            print("INF")
        else:
            print(ans[i])
    