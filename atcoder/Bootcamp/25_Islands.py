""":
How many islands?
わかった
→ アルゴリズムノート(2)のP4に図を記載

方針
・再帰関数版の深さ優先探索で実装する
・Inputがやや癖があるので、各々のケースに対してDFSを適用させる
・一回到達した陸は、重複しないように海にしちゃう

https://atcoder.jp/contests/atc001/tasks/dfs_a
Input
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
Output
9
"""

A = []
h,w = map(int,input().split())
reached = [[False]*w]*h
cnt = 0

for i in range(h):
    A.append(list(map(int,input().split())))

def dfs(xid,yid):
    
    #print(f"Start Checking: xid,yid={xid},{yid}")
    if xid<0 or xid>=h or yid<0 or yid>=w:
        return
    elif reached[xid][yid]:
        A[xid][yid] = 0
        return
    elif A[xid][yid]==0:
        return
    else:
        # この部分に入ってきたものは
        # 壁でも、海でも、既訪問でもないので、探索する
        reached[xid][yid] = True
        A[xid][yid] = 0

        dfs(xid,yid-1)
        dfs(xid,yid+1)

        dfs(xid+1,yid-1)
        dfs(xid+1,yid)
        dfs(xid+1,yid+1)

        dfs(xid-1,yid-1)
        dfs(xid-1,yid)
        dfs(xid-1,yid+1)


for i in range(len(A)):
    for j in range(len(A[i])):
        if not reached[i][j] and A[i][j]==1:
            print(f"i,j = {i},{j}")
            dfs(i,j)
            cnt+=1

print(cnt)
print(A)
print(reached)