"""
nCrを求める問題
一発でいけなかった..
nCrの nとrを以下で求める
・n=総ステップ数=(X+Y)/3
・連立方程式
X = 2s+t
Y = s+2t

「ここ」と書いたところでなかなかACせず。
print(0)条件で、X,Y>=stepをチェックしてないとダメなテストケースが2つあった。
少なくとも、1stepでx座標あるいはy座標は+1されるので、目標点(X,Y)の各値は、
ステップ数以上でないとならない。

"""
def main():
    N = int(1e6)
    MOD = 10**9+7
    X,Y = map(int,input().split())

    fact=[None]*(N+1)
    fact[0]=fact[1]=1
    for i in range(2,N):
        fact[i]=fact[i-1]*i%MOD
    
    def inv(x):
        return pow(x,MOD-2,MOD)

    step = (X+Y)//3
    k = (2*X-Y)//3  #連立方程式立てて計算するとわかる

    # stepCk
    ans = fact[step]*inv(fact[k])%MOD*inv(fact[step-k])%MOD
    if (X+Y)%3!=0 or not X>=step or not Y>=step: ## ここ
        print(0)
    else:
        print(ans%MOD)

if __name__=="__main__":
    main()
