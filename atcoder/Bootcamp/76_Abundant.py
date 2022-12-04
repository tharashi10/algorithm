"""
累積和の基本問題
自力でいけた
4
4 1 3 3
-----
4
6
8
11
"""
from itertools import accumulate
def main():
    N = int(input())
    l = [0] + list(map(int,input().split()))
    acc = list(accumulate(l))

    for k in range(1,N+1):
        ans = 0
        for i in range(N-k+1):
            ans = max(ans,acc[i+k]-acc[i])
        print(ans)
    

if __name__=="__main__" :
    main()
