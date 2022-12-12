"""
12.4 : BFS
--------------------------------
・訪問した頂点vをQueueに入れる
・キューから頂点vを取り出す
・頂点vに隣接する頂点をキューに入れる(ただし未訪問に限る)
・距離行列d[v]を+1する
・空になるまでWhile Loopする
--------------------------------
頂点1からの最短距離dを求める
4
1 2 2 4
2 1 4
3 0
4 1 3
--
1 0
2 1
3 2
4 1
・distをvisitedとマージしたほうがもっと短く投げる
"""

def main():
    N=int(input())
    A = [[0]*N for _ in range(N)]
    for i in range(N):
        ll = list(map(int,input().split()))
        if len(ll)==2:
            continue
        else:
            for x in ll[2:]:
                A[i][x-1]+=1
    
    que = [0] # 最初の頂点をセット（0-Origin）
    visited = [-1]*N
    d = [0 for _ in range(N)]
    
    def bfs():
        while len(que)!=0:
            vid = que.pop(0)
            if visited[vid]!=-1:
                continue
            visited[vid]=1
            
            node = [i for i in range(N) if A[vid][i]==1]
            for u in node:
                if u==0:
                    continue
                if visited[u]!=-1:
                    continue
                d[u]=d[vid]+1
                que.append(u)

    bfs()
    [print(d[i]) for i in range(N)]

if __name__=="__main__":
    main()

