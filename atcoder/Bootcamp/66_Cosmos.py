"""
宇宙ステーションを最小コストで繋ぎたい
Prim法でトライしてみる
はしごの長さは、中心間距離-半径の和

3
10.000 10.000 50.000 10.000
40.000 10.000 50.000 10.000
40.000 40.000 50.000 10.000
20.000
"""
import math
import heapq

def main():
    N = int(input())
    A = []
    for _ in range(N):
        A.append(list(map(float,input().split())))
    
    def distance(p,q):
        dd = 0
        for i in range(3):
            dd+=(p[i]-q[i])**2
        return math.sqrt(dd)-(p[3]+q[3])
    
    G = [[] for _ in range(N)]
    for i in range(N-1):
        for j in range(i+1,N):
            G[i].append((j,distance(A[i],A[j]))) # (node,cost)

    used=[0]*N
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
    
    print(f"{ans:.3f}")

if __name__=="__main__":
    main()
