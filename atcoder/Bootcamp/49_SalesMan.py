"""
巡回セールスマン問題
--Input--
4 6
0 1 2
1 2 3
1 3 9
2 0 1
2 3 6
3 2 4
--Output--
16
"""
import sys
sys.setrecursionlimit(20000)

def rec(bit:int, v:int):
    if dp[bit][v]!='-':      # (A) 既に探索済みなら
        return dp[bit][v]
    
    if bit==(1<<v) : # (B) 初期値 集合S={1}のような場合に相当
        print(f"bit={bit},v={v}")
        dp[bit][v] = 0
        return 0
    
    res=INF
    prev_bit = bit & ~(1<<v) # bit{1,2,3}の時にv=1だとしたら、{2,3}としてprev_bitを決める
    
    for u in range(n):  #(C) 更新の条件
        if (not (prev_bit & (1<<u))): continue # uが集合に含まれてなければ

        if (res > rec(prev_bit,u) + dist[u][v]):
            res = rec(prev_bit,u) + dist[u][v]
    
    dp[bit][v]=res
    return dp[bit][v]

n,m=map(int,input().split())
dist=[]
INF=float('inf')
for i in range(n):
    dist.append([0 for _ in range(n)])

for i in range(m):
    sid,eid,d=map(int,input().split())
    dist[sid][eid]=d

dp=[]
for i in range(30): # 4桁なら1111 = 15
    dp.append(['-' for _ in range(10)])

ans = INF
#for v in range(1):
#    ans = min(ans,rec((1<<n)-1,v)) # (1<<n)-1= 1, 11, 111, 1111, 11111

ans = rec((1<<n)-1,0)
print(ans)
print(dist)
for i in range(20):
    print(*dp[i])