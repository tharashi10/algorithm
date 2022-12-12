"""
Imos法で
4 4
1 3 2 4
120 90 100
110 50 80
250 70 130
--
550
"""
from itertools import accumulate
def main():
    N,M = map(int,input().split())
    P = list(map(int,input().split())) # City
    imos = [0]+[0]*N # 鉄道を使う回数

    A=[]
    B=[]
    C=[]
    for i in range(N-1):
        a,b,c = map(int,input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    
    for i in range(M-1):
        if P[i]<P[i+1]:
            imos[P[i]]+=1
            imos[P[i+1]]-=1
        else:
            imos[P[i+1]]+=1
            imos[P[i]]-=1
    cum = list(accumulate(imos))
    ans = 0
    for i in range(1,N): # 鉄道iでLoop
        cnt = cum[i]
        ans += min(cnt*A[i-1],cnt*B[i-1]+C[i-1])
    print(ans)

if __name__=="__main__":
    main()
