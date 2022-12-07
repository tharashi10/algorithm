"""
2次元累積和
H W K V
1 1 200 500
300
--
300 + K*1 = 500 <=500
->1
"""
from itertools import accumulate
def main():
    H,W,K,V=map(int,input().split())
    C = [[0]*(W+1) for _ in range(H+1)]
    for i in range(H):
        C[i+1][1:]=list(map(int,input().split()))
    
    def transpose(X):
        return list(map(list,zip(*X)))
    
    def acc(X):
        for i in range(H):
            X[i+1] = list(accumulate(X[i+1]))
        return X
    C = acc(C)
    C = transpose(C)
    C = acc(C)
    C = transpose(C)

    ans = 0
    for i in range(1,H+1):
        for j in range(i+1,H+2):
            for k in range(1,W+1):
                for l in range(k+1,W+2):
                    # [i,j) [k,l)
                    tmp = (j-i-2)*(l-k-2)*K + C[j-1][l-1]-C[i-1][l-1]-C[j-1][k-1]+C[i-1][k-1]
                    if tmp<=V:
                        ans = max(ans,(j-1-i-1)*(l-1-k-1))
                    print(f"ans:{ans}")
                    print(f"[{i-1},{j-1}) : [{k-1},{l-1})")

if __name__=="__main__":
    main()
