
"""
二次元累積和
PythonだとTLEするs
2次元の累積和のロジックをつかめればよしとする
ACしたいならC++で

10個中5個ACできる

https://kakedashi-engineer.appspot.com/2020/06/20/joi2011hoa/

4 7
4
JIOJOIJ
IOJOIJO
JOIJOOI
OOJJIJO
3 5 4 7
2 2 3 6
2 2 2 2
1 1 4 7
--
1 3 2
3 5 2
0 1 0
10 11 7
"""
from itertools import accumulate
def main():
    H,W = map(int,input().split())
    M = int(input())
    A = [[None]*W for i in range(H)]
    J = [[0]*(W+1) for i in range(H+1)]
    O = [[0]*(W+1) for i in range(H+1)]
    I = [[0]*(W+1) for i in range(H+1)]
    sum_j = []
    sum_o = []
    sum_i = []

    def transpose(l):
        return list(map(list,zip(*l)))
    
    for i in range(H):
        st = str(input())
        for j in range(W):
            A[i][j]=st[j]
    
    for i in range(H):
        for j in range(W):
            if A[i][j]=='J':
                J[i+1][j+1]+=1
            elif A[i][j]=='O':
                O[i+1][j+1]+=1
            else:
                I[i+1][j+1]+=1
    
    def trans(X):
        Y = []
        for x in X:
            Y.append(list(accumulate(x)))

        cum_sum = []
        Y = transpose(Y)
        for y in Y:
            cum_sum.append(list(accumulate(y)))
        
        cum_sum = transpose(cum_sum)
        return cum_sum

    J = trans(J)
    O = trans(O)
    I = trans(I)

    query = []
    for i in range(M):
        query.append(map(int,input().split()))

    for q in query:  # 区間[a,b) , [c,d)
        a,c,b,d = q
        a-=1
        c-=1
        ans_j = J[b][d]-J[a][d]-J[b][c]+J[a][c]
        ans_o = O[b][d]-O[a][d]-O[b][c]+O[a][c]
        ans_i = I[b][d]-I[a][d]-I[b][c]+I[a][c]
        print(ans_j,ans_o,ans_i)

if __name__=="__main__":
    main()
