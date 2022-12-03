"""
重複順列
nHr= n+r-1Cr
自力で行けた
"""

def main():
    n = int(input())
    k = int(input())
    MOD = int(1e9+7)
    M = 2*int(1e5)

    fact = [None]*M
    fact[0]=fact[1]=1
    for i in range(2,M):
        fact[i]=fact[i-1]*i%MOD

    def inv(x):
        return pow(x,MOD-2,MOD)
    
    ans = fact[n+k-1]*(inv(fact[k])%MOD)*(inv(fact[n-1])%MOD)
    print(ans%MOD)

if __name__=="__main__":
    main()
