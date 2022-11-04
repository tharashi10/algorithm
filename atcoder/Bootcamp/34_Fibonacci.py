"""
・自力で行けた。09分
input
3
Output
3
"""

m = int(input())
dp = [-1 for _ in range(10**7)]

def func(n):
    if n == 0 or n==1:
        return 1
    
    if dp[n]!=-1:
        return dp[n]
    else:
        dp[n]=func(n-1)+func(n-2)
        return dp[n]

print(func(m))
    