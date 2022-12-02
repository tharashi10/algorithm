"""
冪乗を高速に計算する
→ べきを2進数に変換して、逐次2乗していく
https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a#4-累乗-an

mod=1,000,000,007 (10億7)
2 3
8
"""

def main():
    # aのn乗を計算するが、値が大きくなるのでmod計算する
    def modpow(a,n,mod):
        res = 1
        while (n>0):
            if n&1:
                res=(res*a%mod)
            a*=a%mod
            n>>=1 # 代入演算子で
        return res

    mod=1000000007
    a,n = map(int,input().split())
    print(modpow(a,n,mod))

if __name__=="__main__":
    main()
