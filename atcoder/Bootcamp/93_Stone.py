"""
パスする
色んな人の提出結果を見るとPyPyを使っている模様
C++でやった方がいいかも
石落としゲーム
[TODO]
・92と違う点として連続する文字数が任意(Kへの対応)
・スコア計算が段落としの回数に依存する(Score計算)

4 4 2
3413
4121
1424
2312
"""

def main():
    # 標準入力
    H,W,K = map(int,input().split())
    table = []
    memo = [False for _ in range(W)]*H
    for i in range(H):
        st=str(input())
        tmp = [int(s) for s in st]
        table.append(tmp)
    table = list(reversed(table))

    # ひとつマスを消す
    for i in range(H):
        for j in range(W):
            if i==0 and j==2:
                table[i][j]=0
    
    # memo表にT/Fを書き入れる
    def flip(table,memo):
        for i in range(H):
            for j in range(W):
                if table[i][j]==0:
                    memo[i][j]=True
    
    # 表における0を埋める(落とす作業). 但し一段面
    def format(table,memo):
        cnt = -1
        for j in range(W):
            for i in range(H):
                for k in range(H-i-1):
                    if table[k][j]==0:
                        table[k][j]=table[k+1][j]
                        table[k+1][j]=0
    
    format(table,memo)
    print(table)

if __name__=="__main__":
    main()
