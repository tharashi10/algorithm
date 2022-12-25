"""
Chain Disappearance Puzzle
落ちものパズルゲームの実装
PseudoCode
3つ連続する部分は0に置き換える
置き換えた後、一つ上の行の値を置き換える
落とされた後、上段の数が0になる

石を落下させる部分を考えさせられた。
また、テストケース1007個のうち、1つだけ合わないものがあったのでDebugした。
250個目のやつと特定した。
# 3 6 4 9 9 ->  0 0 0 9 9 -> 0 0 0 0 0
# 4 4 9 5 8 ->  3 6 4 5 8 -> 3 6 0 9 9
# 6 6 6 9 9 ->  4 4 9 9 9 -> 4 4 4 5 8
# 18 + 27 + 12 = 57

-----------A[ij]
40 41 42 43 44 
30 31 32 33 34 
20 21 22 23 24 
10 11 12 13 14 
00 01 02 03 04 
-------------- index設定 の イメージ
0 69 24 87 27
5
5 9 5 5 9 -> 5 9 5 5 9 -> 5 9 0 0 0 -> 5 9 0 0 0 -> 0 0 0 0 0
5 5 6 9 9 -> 5 5 6 9 9 -> 5 5 5 5 9 -> 0 0 0 0 9 -> 0 0 0 0 9
4 6 3 6 9 -> 4 6 3 6 9 -> 4 6 6 9 9 -> 4 6 6 9 9 -> 0 0 0 9 9
3 3 2 9 9 -> 3 3 2 9 9 -> 3 3 3 6 9 -> 0 0 0 6 9 -> 5 9 0 6 9
2 2 1 1 1 -> 2 2 0 0 0 -> 2 2 2 9 9 -> 0 0 0 9 9 -> 4 6 6 9 9
--
38
"""

def main():
    
    # 2Dテーブルに対して、連続している箇所をTrueにする
    def flip(table,memo):
        for i in range(N):
            for j in range(1,M-1):
                if table[i][j]!=0 and table[i][j-1]==table[i][j]==table[i][j+1]:
                    memo[i][j-1]=True 
                    memo[i][j]  =True
                    memo[i][j+1]=True
                    
    # 得点計算 : Trueのものを加算し、計算し終えたものは0にする
    def score(table,memo):
        score_tmp = 0
        for i in range(N):
            for j in range(M):
                if memo[i][j]:
                    score_tmp+=table[i][j]
                    table[i][j]=0
        return score_tmp
    
    # 複数段落とす(Bubble Sort)
    def table_format(table):
        for j in range(M):     # ある列jに対して
            for i in range(N): # ある行iに対して
                for k in range(N-i-1): # バブルソートなので末尾から決まっていくイメージ
                    if table[k][j]==0:
                        table[k][j]=table[k+1][j]
                        table[k+1][j]=0                    
    
    while(True):
        # stdin
        N = int(input())
        M = 5
        
        table = []
        if N==0:
            break
        for _ in range(N):
            table.append(list(map(int,input().split())))
        
        ans = 0
        table = list(reversed(table))
        
        if N==1: # 落とす回数は0回
            memo = [[False]*M for _ in range(N)]
            flip(table,memo)
            ans+=score(table,memo)
        else:
            for _ in range(N): # 落とす動作は最大N-1回
                memo = [[False]*M for _ in range(N)] #memoは毎度初期化
                flip(table,memo)
                ans+=score(table,memo)
                table_format(table)

    print(ans)

if __name__=="__main__":
    main()
