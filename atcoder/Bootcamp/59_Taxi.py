"""
Taxi

Submissionから参考になりそうなものを拝借して理解した
https://atcoder.jp/contests/joi2014yo/tasks/joi2014yo_e

本文をPython3でやる場合、TLEになるのが普通なので、
ACしたければ、Cppでやる直すのが吉

6 6
400 2
200 1
600 3
1000 1
300 5
700 4
1 2
2 3
3 6
4 6
1 5
2 4
--
700
"""
import heapq
import collections

def main():
    V,E = map(int,input().split())
    CR = [[0,0]]+[ list(map(int,input().split())) for _ in range(V) ]
    
    # グラフ作成
    G = [ [] for _ in range(V+1) ]
    for i in range(E):
        s,t = map(int,input().split())
        G[s].append(t)
        G[t].append(s)

    # コストを加味したグラフ作成
    newG = [ [] for _ in range(V+1) ]
    for i in range(1,V):
        dist = [-1]*(V+1)
        dist[i]=0
        queue = collections.deque()
        queue.append(i)

        # BFS
        while queue:
            q = queue.popleft()

            if not G[q]:
                continue
            for x in G[q]: # 隣接するノードに対して
                if dist[x] == -1: # 未到達ノードに対して
                    dist[x] = dist[q]+1 
                    if dist[x]<=CR[i][1]: # Taxiを使える最大ステップを超えなければ
                        newG[i].append(x)
                        queue.append(x)

    #print(CR)
    #print(newG)
    #メモリ解法
    del G,queue

    # ダイクストラ法
    heap = []
    heapq.heappush(heap,(0,1))
    dist = [1e20]*(V+1)
    seen = [False]*(V+1)

    while heap:
        pre_cost,pre = heapq.heappop(heap)
        if seen[pre]:
            continue
        seen[pre]=True

        cost = CR[pre][0]
        for to in newG[pre]:
            if seen[to]==False and dist[to]>pre_cost+cost:
                dist[to] = pre_cost+cost
                heapq.heappush(heap,(dist[to],to))
    print(dist[V])

if __name__=='__main__':
    main()