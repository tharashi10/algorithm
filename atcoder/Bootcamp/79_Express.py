"""
二次元累積和
C[L][R] = 区間[L,R)にある列車の個数

2次元の場合、累積和出すまでは簡単だが、最後のAnsを計算するときの、
区間とIndexのMappingで考えてしまう。
時間かかったが、ACできた。

クエリ[1 2]ときたとき、
区間[1,3) × 区間[1,3) の累積和を事前に計算した累積和Matrixから引き算で算出する。
その際以下のような引き算になる。

対象領域の累積和 = C[2][2] - C[0][2] - C[2][0] + C[0][0]
↑ x座標のみ -1 にして、行列のIndexに落とし込むようにしている

また、もう一つのポイントとして、区間Indexは、行列の区画(ex. 1行目と2行目の間の線をindex=1)
としてみていることに注意。

2 3 1
1 1
1 2
2 2
1 2
--
3
"""
from itertools import accumulate

def main():
    N,M,Q = map(int,input().split())
    C = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        L,R = map(int,input().split())
        C[L][R]+=1
    
    for i in range(N+1):
        C[i]=list(accumulate(C[i]))
    
    def transpose(X):
        return list(map(list,zip(*X)))
    
    C = transpose(C)
    for i in range(N+1):
        C[i]=list(accumulate(C[i]))
    C = transpose(C)

    query = [list(map(int,input().split())) for _ in range(Q)]
    for i in range(Q):
        x, y = query[i][0]-1, query[i][1]  # TestCase1の時 (x,y)=(0,2)
        print(C[y][y]-C[y][x]-C[x][y]+C[x][x])

if __name__=="__main__":
    main()
