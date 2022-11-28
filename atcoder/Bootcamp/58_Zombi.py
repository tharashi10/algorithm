"""
ダイクストラ
方針
・隣接リスト作る
・作った隣接リストで、Zombi町にSステップ以内につながる危険な町リストを作る
・安全町リストも作り、たどり着いた町が安全町リストに含まれるならP円、含まれないならQ円と分岐する
・町1から開始点として、町Nまでダイクストラした時の距離(宿泊代)の最小値をOutputする

・到達可能性検証といえばBFS。→ ゾンビ島からKステップで到達できる島を見つける

13 21 1 1
1000 6000
7
1 2
3 7
2 4
5 8
8 9
2 5
3 4
4 7
9 10
10 11
5 9
7 12
3 6
4 5
1 3
11 12
6 7
8 11
6 13
7 8
12 13
---
11000
"""
import heapq

def main():
    V,E,K,S = map(int,input().split())
    P,Q = map(int,input().split())
    C = [int(input()) for i in range(K)]
    G = [[] for _ in range(V+1)]

    dic = {}
    INF = 10**10

    for _ in range(E):
        s,t = map(int,input().split())
        G[s].append(t)
        G[t].append(s)
    
    # bfs part
    for c in C:
        que = [c]
        dist = [-1]*(V+1)
        dist[c] = 0
        while len(que)!=0:
            vid = que.pop(0)
            for v in G[vid]:
                if dist[v]!=-1:
                    continue
                if (dist[vid]+1) > S:
                    break
                dist[v] = (dist[vid]+1)
                que.append(v)
    
    danger = []
    for i in range(len(dist)):
        if 0<=dist[i]<=S:
            danger.append(i)

    # Dijkstra part
    start, goal = 1,V
    sum_dist = [INF]*(V+1)
    sum_dist[start]=0
    ans = dijkstra(start, G, sum_dist, danger, P, Q, C)

    if ans[goal] != INF:
        print(ans)
        print(C)
    else:
        print(f"-1")

def dijkstra(s,G,sum_dist,danger,P,Q,C):
    hq = [(0,s)] # (Weight, Node)
    while hq:
        cost, now = heapq.heappop(hq)
        for next in G[now]:
            if next in C:
                continue
            
            if next in danger:
                tmp = cost + Q
            else:
                tmp = cost + P
            
            if tmp < sum_dist[next]:
                sum_dist[next] = tmp
                heapq.heappush(hq,(tmp,next))
    return sum_dist


if __name__ == "__main__":
    main()