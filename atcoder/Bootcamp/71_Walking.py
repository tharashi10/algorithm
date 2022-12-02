"""
冪乗の高速計算は書けた
累積和を使うといいらしい

・pow(a,n,MOD)のライブラリもあるぽい
・from itertools import accumulate使うと一撃で累積和作れちゃう

4 3
5 3 1 2
3 2 4
264
"""
from itertools import accumulate

def main():
    
    def modpow(a,n,mod):
        res = 1
        while(n>0):
            if n&1:
                res = res*a%mod
            a*=a%mod
            n>>=1
        return res
    
    N,Q = map(int,input().split())
    CumSum = [0]  # 街0から街iまでの距離を蓄積する

    MOD = 10**9+7
    P = list(map(int,input().split()))
    Route = [1] + list(map(int,input().split())) + [1]
    
    for i in range(N-1):
        d = modpow(P[i],P[i+1],MOD)
        CumSum.append(d)
    acc = list(accumulate(CumSum))
    
    ans = 0
    for j in range(len(Route)-1):
        s_idx = Route[j]-1
        t_idx = Route[j+1]-1    # Routeには、1-indexedで格納されている
        ans+=abs(acc[t_idx]-acc[s_idx])%MOD

    print(ans%MOD)  # 最後の%MODを忘れてハマった...

if __name__=="__main__":
    main()
