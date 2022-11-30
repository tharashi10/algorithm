"""
こちらも一旦ワーシャルフロイドを書く
TLEになった。
問題文がいまいちすんなり入らない。かつTLEになるので一旦OK。

3
0 1 3 
1 0 2
3 2 0
--
3
"""

def main():
    N = int(input())
    A = [[float('inf')]*N for _ in range(N)]

    for u in range(N):
        l = list(map(int,input().split()))
        
        for v in range(N):
            if u==v:
                continue
            A[u][v]=l[v]
    
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            mn = float('inf')
            for k in range(N):
                mn = min(mn,A[i][k]+A[k][j])
            
            if A[i][j] > mn:
                print("-1")
                return
            elif A[i][j] < mn:
                ans += A[i][j]

    print(ans)

if __name__=="__main__":
    main()
