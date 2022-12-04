"""
旅人
累積和
これも余裕

7 5
2
1
1
3
2
1
2
-1
3
2
-3
ans=18
"""

from itertools import accumulate

def main():
    N,M = map(int,input().split())
    l = [0,0]+[int(input()) for i in range(N-1)]
    t = [int(input()) for i in range(M)]
    acc = list(accumulate(l))
    MOD = int(1e5)

    ans = 0
    now = 1
    for i in range(M):
        next = now + t[i] # 3
        ans+=abs(acc[next]-acc[now])%MOD
        now = next
    
    print(ans%MOD)

if __name__=="__main__":
    main()
