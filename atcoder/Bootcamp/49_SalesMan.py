"""
巡回セールスマン問題(Traveling Salesman: TSP)
https://cnc-selfbuild.blogspot.com/2019/05/tsp-dp.html
集合はsetでもOKぽいが、intで2進数のbitでやるのがメインアプローチぽいので
それでやってみる

https://www.slideshare.net/hcpc_hokudai/advanced-dp-2016
https://qiita.com/kiura_369/items/d9e7853341a8405a898f

dp[S][v]:=頂点0からスタートして、
{0,1,2,3,...,n-1}の部分集合Sを巡回する|S|!通りの経路のうち最短のものの距離.
ただし、最後に頂点vに達した時のみを考える.

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

# int bit, int v
def rec(bit, v):
    if dp[bit][v]!='-':      # (A) 既に探索済みならメモ値を返す
        return dp[bit][v]

    #if bit==0:
    #    return 0
    
    #if bit==(1<<v):          # (B) 初期値 集合S={1}のような場合に相当
    #    print(f"bit={bit},v={v}")
    #    dp[bit][v] = 0
    #    return 0
    
    res=INF
    prev_bit = bit & ~(1<<v) # bit{1,2,3}の時にv=1だとしたら、{2,3}としてprev_bitを決める
    print(f"prev_bit: {prev_bit}")
    for u in range(n):  #(C) 更新の条件
        if (not (prev_bit & (1<<u))): 
            continue # uが集合に含まれてなければ

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
for i in range((1<<6)+1): # dpテーブルは余裕をもったサイズにする
    dp.append(['-' for _ in range(10)])

dp[0][0]=0
ans = INF
##for v in range(1):
#    ans = min(ans,rec((1<<n)-1,v)) # (1<<n)-1= 1, 11, 111, 1111, 11111

ans = rec((1<<n)-1,0)
print(ans)

for i in range(20):
    print(*dp[i])
