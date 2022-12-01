"""
宇宙ステーションを最小コストで繋ぎたい
Prim法でトライしてみる
はしごの長さは、中心間距離-半径の和

なんとか行けた。
N=1の時でreturn Noneして、全然ACせず。外してAC済み

3
10.000 10.000 50.000 10.000
40.000 10.000 50.000 10.000
40.000 40.000 50.000 10.000
20.000
--
2
30.000 30.000 30.000 20.000
40.000 40.000 40.000 20.000
5
5.729 15.143 3.996 25.837
6.013 14.372 4.818 10.671
80.115 63.292 84.477 15.120
64.095 80.924 70.029 14.881
39.472 85.116 71.369 5.553
0
"""

import math
import heapq

def main():
    while True:
        N=int(input())
        if N==0:
            break
        #elif N==1:
        #    print(f"{0:.3f}")
        #    exit()

        A = []
        for _ in range(N):
            A.append(list(map(float,input().split())))
    
        def distance(p,q):
            dd = 0
            for i in range(3):
                dd+=(p[i]-q[i])**2
            tmp = math.sqrt(dd)-(p[3]+q[3])
            if tmp <=0:
                return 0
            else:
                return tmp
    
        G = [[] for _ in range(N)]
        for i in range(N-1):
            for j in range(i+1,N):
                G[i].append((j,distance(A[i],A[j]))) # (node,cost)
                G[j].append((i,distance(A[i],A[j]))) # (node,cost)

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
