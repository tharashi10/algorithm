"""
Warshall Floyd
一旦DP作ってみる作戦で

最後のAnsを出す時の大小比較で、INFが邪魔になる
PythonだとやはりTLEする。これは仕方なし。ロジックあってるのでOK
ACしたいならC++でファイ
39ケースあるうちの2つ目で既にぐるぐるなってTLEマーク付いたからだいぶ遅いんだと思う

--Input
3 2
1 2 10
2 3 10
--Output
10
"""

def main():
    V,E = map(int,input().split())
    dp = [[float('inf')]*(V+1) for _ in range(V+1)]

    for i in range(V+1):
        dp[i][i]=0

    for _ in range(E):
        s,t,w = map(int,input().split())
        dp[s][t]=w
        dp[t][s]=w

    # WF
    for k in range(V+1):
        for i in range(V+1):
            for j in range(V+1):
                dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])
    
    ans = 10**10
    for i in range(1,V+1):
        l = [s for s in dp[i] if s!=float('inf')]
        ans = min(ans,max(l))
    
    print(ans)
    
if __name__=="__main__":
    main()
