"""
得点を算出する問題(A)
In/
5 3
Out/
7
----
愚直に書いた。
・重複リストをどうすればいいのか
・順序考慮なしの場合のリスト一致がすぐに思いつかなかった
(比較する際にSetに戻してあげればいいだけ)
"""

def solve():
    return None

if __name__== "__main__":
    A, B = map(int,input().split())
    #print(A,B)
    l = [[0,[]],
         [1,['A']],
         [2,['B']],
         [3,['A','B']],
         [4,['C']],
         [5,['A','C']],
         [6,['C','B']],
         [7,['A','B','C']]]
    p = set(l[A][1] + l[B][1])
    pl =list(p)
    for i in range(0,len(l)):
        #print(l[i][1])
        if set(l[i][1]) == set(pl):
            print(l[i][0])
