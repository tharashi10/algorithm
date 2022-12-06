"""
二次元累積和

C[L][R] = 区間[L,R)にある列車の個数 

2 3 1
1 1
1 2
2 2
1 2
--
3
"""
from itertools import accumulate

def main():
    N,M,Q = map(int,input().split())
    C = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        L,R = map(int,input().split())
        C[L][R]+=1
    
    def solve(L,R):
        for i in range(N+1):
            C[i]=list(accumulate(C[i]))
    
        def transpose(X):
            return list(map(list,zip(*X)))
    
        C = transpose(C)
        for i in range(N+1):
            C[i]=list(accumulate(C[i]))
        C = transpose(C)

        return C[r][r]

    query = [list(map(int,input().split())) for _ in range(Q)]
    for i in range(Q):
        L,R = query[i][0],query[i][1]
        print(C[R][R]-C[L][L])

if __name__=="__main__":
    main()
