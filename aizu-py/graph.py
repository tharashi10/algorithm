''':
隣接行列を作る
TIPSその1: 二次元配列の初期化: [[0]*N]*M
TIPSその2: 多次元配列を上記のようにつくると、要素のリストが全て同一Objectとなる
そうなると、特定の行列の値を更新する際に別の要素も更新されてしまう。
したがって、以下のように多次元配列を作成する(リスト内包記)
2dArray = [[]*3 for i in range(3)]
'''
def convertAdjList(A, N):
    adjacentList = [[0]*N for _ in range(N)]
    
    for i in range(N):
        for k in range(A[i][1]):
            node_idx = A[i][k+2]-1
            adjacentList[i][node_idx]=1
    
    return adjacentList

def printAdjacent(list2d, N):
    for i in range(N):
        for j in range(N):
            if (j!=N-1):
                print(list2d[i][j], end=' ')
            else:
                print(list2d[i][j])

N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))

printAdjacent(convertAdjList(A,N),N)
