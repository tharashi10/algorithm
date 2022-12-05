"""
二次元累積和

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


--
4 7
1
JIOJOIJ
IOJOIJO
JOIJOOI
OOJJIJO
3 5 4 7
"""

def main():
    H,W = map(int,input().split())
    M = int(input())
    A = [[None]*W for i in range(H)]
    sum_j = [[0]*(W+1) for i in range(H+1)]
    sum_o = [[0]*(W+1) for i in range(H+1)]
    sum_i = [[0]*(W+1) for i in range(H+1)]
    
    for i in range(H):
        st = str(input())
        for j in range(W):
            A[i][j]=st[j]
    
    for i in range(H):
        for j in range(W):
            if A[i][j]=='J':
                sum_j[i+1][j+1]+=1
            elif A[i][j]=='O':
                sum_o[i+1][j+1]+=1
            else:
                sum_i[i+1][j+1]+=1
    
    for i in range(H):
        for j in range(W):
            tmp_j = 0
            if A[i][j]=='J':
                tmp_j+=1
            sum_j[i+1][j+1]= sum_j[i][j+1]+sum_j[i+1][j]-sum_j[i][j]+tmp_j
            
            tmp_o = 0
            if A[i][j]=='O':
                tmp_o+=1
            sum_o[i+1][j+1]= sum_o[i][j+1]+sum_o[i+1][j]-sum_o[i][j]+tmp_o
            
            tmp_i = 0
            if A[i][j]=='I':
                tmp_i+=1
            sum_i[i+1][j+1]= sum_i[i][j+1]+sum_i[i+1][j]-sum_i[i][j]+tmp_i

    print("Query")
    
    for i in range(M):
        a,c,b,d = map(int,input().split())
        # 区間[a,b) , [c,d)
        
        #print(f"a,b,c,d={a,b,c,d}")
        #print(f"sum_max:{sum_j[4][7]}")
        #print(f"sum_max:{sum_j[4][5]}")
        #print(f"sum_max:{sum_j[3][7]}")
        #print(f"sum_max:{sum_j[3][5]}")
        #print(f"sum:{sum_j[b][d],sum_j[a][d],sum_j[b][c],sum_j[a][c]}")

        ans_j = sum_j[b][d]-sum_j[a][d]-sum_j[b][c]+sum_j[a][c]
        ans_o = sum_o[b][d]-sum_o[a][d]-sum_o[b][c]+sum_o[a][c]
        ans_i = sum_i[b][d]-sum_i[a][d]-sum_i[b][c]+sum_i[a][c]
        print("***************")
        print(ans_j,ans_o,ans_i)

if __name__=="__main__":
    main()
