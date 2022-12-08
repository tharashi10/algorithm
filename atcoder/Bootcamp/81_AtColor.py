"""
Imos法
自力で行けた
https://imoz.jp/algorithms/imos_method.html

4
0 2
2 3 
2 4 
5 6
--
3
"""
from itertools import accumulate
def main():
    N = int(input())
    Q = []
    [ Q.append(list(map(int,input().split()))) for _ in range(N) ]

    M = 2*int(1e6)
    C = [0]*M
    for i in range(N):
        start = Q[i][0]
        end = Q[i][1]
        C[start]+=1
        C[end+1]-=1
    C = list(accumulate(C))

    def tranpose(X): # 1Dなので使わない
        return list(map(list, zip(*X)))
    
    print(max(C))

if __name__=="__main__":
    main()
