"""
modの基本は下記のURLで
https://www.creativ.xyz/modulo-basic/

高速累乗計算は、#70で実装・学習済み
math.factorial(n)で計算するとTLEになる
→そのため、逆元+Fermatの小定理(またはEuclid)で実装

・max_N = 2*10**5にしないとTLEする
・fact_invの配列も用意するとTLEする(C++なら通るそう)

4 3
10
"""
def main():
    MOD=10**9+7
    def modpow(a,n,mod):
        """
        繰り返し2乗法
        """
        res = 1
        while n>0:
            if n&1:
                res=(res*a%MOD)
            a*=a%MOD
            n>>=1
        return res

    N = 2*int(1e5)
    fact = [None]*(N+1)

    fact[0]=fact[1]=1
    for i in range(2,N+1):
        fact[i]=fact[i-1]*i%MOD

    def inv(x):
        return modpow(x,MOD-2,MOD)

    def cmb(n,k):
        return fact[n]*(inv(fact[n-k])%MOD*inv(fact[k]))%MOD
    
    W,H=map(int,input().split())
    print(cmb(W+H-2,W-1))

if __name__=="__main__":
    main()
