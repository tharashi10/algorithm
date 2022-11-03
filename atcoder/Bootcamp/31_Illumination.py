"""
方針:
・周囲を0埋めする
・白マスと黒マスの境界を全部足し合わせればOk
・BFSは3方向だけで、OKかと思ったけど、6方向必要な模様
・分岐の書き方工夫→ if val%2==0: ...同じ処理を2回書かないようにリストで分岐させる
・時間かかったところとして、dxdyリストを書きミスっていた。。。ちゃんと6方向の図書くべし

8 4
0 1 0 1 0 1 1 1
0 1 1 0 0 1 0 0
1 0 1 0 1 1 1 1
0 1 1 0 1 0 1 0
--
64
"""
w,h = map(int,input().split())
A = [[0 for _ in range(w+2)]]
for i in range(h):
    tmp = [0]
    tmp+=list(map(int,input().split()))
    tmp.append(0)
    A.append(tmp)
A.append([0 for _ in range(w+2)])

direct_odd = [[-1,0],[1,0],[0,1],[1,-1],[0,-1],[1,1]] #←ここ
direct_even = [[-1,0],[1,0],[-1,1],[0,1],[-1,-1],[0,-1]] #←ここ

que = [[0,0]]
visited = []

for i in range(h+2):
    visited.append([0 for _ in range(w+2)])

def bfs(sx,sy):
    cnt = 0
    visited[sx][sy] = 1
    while len(que)!=0:
        v = que.pop(0)

        if v[1]%2==0:
            dxdy = direct_even
        else:
            dxdy = direct_odd
        
        for d in dxdy:
            x = v[0]+d[0] 
            y = v[1]+d[1]

            if not (0<=x<w+2) or not (0<=y<h+2):
                continue
                
            if A[y][x]==1:
                cnt+=1
                #print(f"[even]v[0],v[1]:{v[0]},{v[1]}")
                
            if visited[y][x]==1 or A[y][x]==1:
                continue

            visited[y][x]=1
            que.append([x,y])

    return cnt
print(bfs(0,0))
