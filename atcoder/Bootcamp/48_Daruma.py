"""
だるま落とし
方針:
・区間DP
・dp[l][r]:= 区間[l,r)で、取り除くことができる最大のブロックの数
・ex. w={1,2,3,4}の時
--------------------------
  r=0  1  2  3  4
w=3 0  0  2  2  4←こいつがAnsになる(dp[0][4])
w=2 0  0  0  2  2 
w=1 0  0  0  0  2
w=0 0  0  0  0  2
--------------------------

・再帰で書く方が良いらしい
・TLEになったけど、一旦OK(ボトムアップなら通る可能性大.C++なら再帰で通る)

4
1 2 3 4
4
1 2 3 1
5
5 1 2 3 6
14
8 7 1 4 3 5 4 1 6 8 10 4 6 5
5
1 3 5 1 3
0
---
4
4
2
12
0
"""

def recur(l,r):
    if dp[l][r]!=-1:
        return dp[l][r]
    if abs(l-r)<=1:
        return 0
    result = 0

    # ptn1
    if abs(w[l]-w[r-1])<=1 and recur(l+1,r-1)==r-l-2:
        result=r-l
    
    # ptn2
    if result==0:
        for mid in range(l+1,r-1):
            result=max(result, recur(l,mid)+recur(mid,r))
    
    dp[l][r]=result
    return result

ans = []
while True:
    n = int(input())
    if n==0:
        for i in range(len(ans)):
            print(ans[i])
        break
    w = list(map(int,input().split()))
    dp=[]
    
    for i in range(len(w)):
        dp.append([-1 for j in range(n+1)])
    
    recur(0,n)
    ans.append(dp[0][n])

