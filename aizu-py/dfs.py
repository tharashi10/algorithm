'''
Depth First Search:深さ優先探索
'''
# Graph.pyから引継ぐ
def convertAdjList(A, N):
    adjacentList = [[0]*N for _ in range(N)]
    
    for i in range(N):
        for k in range(A[i][1]):
            node_idx = A[i][k+2]-1
            adjacentList[i][node_idx]=1
    
    return adjacentList

def dfs(matrix, timestamp_d, timestamp_f, now, count):
    # 既出の場合は、何もせずに飛ばす
    #print("timestamp_d[now] : %s " % timestamp_d[now])
    if timestamp_d[now]!=0:
        return count

    # 未出の場合は、子を更にサーチする
    count +=1
    timestamp_d[now] = count
    for i in range(len(matrix)):
        if matrix[now][i]==1:
            count = dfs(matrix, timestamp_d, timestamp_f,i,count)

    #  隣接リストの調査済み時間を記録する
    # 隣接する未訪問ノードが存在しない場合
    count +=1
    timestamp_f[now] = count
    return count

if __name__ == "__main__":
    N = int(input())
    A = []
    for _ in range(N):
        A.append(list(map(int,input().split())))

    matrix = convertAdjList(A,N)
    timestamp_d = [0 for _ in range(N)]
    timestamp_f = [0 for _ in range(N)]
    count = 0

    for j in range(N):
        count = dfs(matrix, timestamp_d, timestamp_f, j, count)

    for k in range(N):
        print(str(k+1) + " " + str(timestamp_d[k]) + " " + str(timestamp_f[k]))