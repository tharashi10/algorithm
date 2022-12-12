"""
12.2 : [基本]隣接行列を求める
--------------------------------
隣接行列の特徴として
(長所) 頂点u,vの関係を、O(1)で計算可能
(短所) Nの2乗のメモリを確保するため、疎なグラフの場合無駄遣いをする
--------------------------------
4
1 2 2 4
2 1 4
3 0
4 1 3
--
0 1 0 1
0 0 0 1
0 0 0 0 
0 0 1 0
"""

def main():
    N=int(input())
    A = [[0]*N for _ in range(N)] 
    for i in range(N):
        l = list(map(int,input().split()))
        if len(l)==2:
            continue
        else:
            for x in l[2:]:
                A[i][x-1]+=1
    [print(*A[i]) for i in range(len(A))]

if __name__=="__main__":
    main()
