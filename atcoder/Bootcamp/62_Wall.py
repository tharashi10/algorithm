"""
一旦黙ってWarshall Floydを書いてみる
自力でACできた

2 4
0 9 9 9 9 9 9 9 9 9
9 0 9 9 9 9 9 9 9 9
9 9 0 9 9 9 9 9 9 9
9 9 9 0 9 9 9 9 9 9
9 9 9 9 0 9 9 9 9 2
9 9 9 9 9 0 9 9 9 9
9 9 9 9 9 9 0 9 9 9
9 9 9 9 9 9 9 0 9 9
9 9 9 9 2 9 9 9 0 9
9 2 9 9 9 9 9 9 9 0
-1 -1 -1 -1
8 1 1 8
---
12
"""

def main():
    H,W = map(int,input().split())
    dp = [list(map(int,input().split())) for _ in range(10)]
    wall = [list(map(int,input().split())) for _ in range(H)]

    for k in range(10):
        for i in range(10):
            for j in range(10):
                dp[i][j] = min(dp[i][j],dp[i][k]+dp[k][j])

    ans = 0
    for i in range(H):
        ll = [ s for s in wall[i] if s!=-1 ]
        if len(ll)==0:
            continue
        else:
            for m in ll:
                ans += dp[m][1]
    
    print(ans)

if __name__ == "__main__":
    main()
