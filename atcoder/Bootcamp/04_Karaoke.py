""":
Karaoke
M 曲の中から 2つの曲を選ぶ(それぞれT1,T2とする)
それぞれの生徒が曲T1,T2の両方を歌う.
各生徒の得点はその生徒が歌った2つの曲の点数のうち高い方となる
グループの得点は生徒1,2,...,N の得点の合計となる.
そのときグループの得点として考えられる最大の値を求めてください.
Input: 
1 2
80 84
-----
Output
84
---
実行速度: 235 ms
"""

n, m = input().split()
score_lst =  []
for i in range(int(n)):
    score = list(map(int,input().split())) 
    score_lst.append(score)

def getMaxScoreList(lst,n,m):
    max_score_lst = []
    
    for j in range(int(m)):
        if j==int(m)-1:
            break
        for jj in range(j+1,int(m)):
            max_two_song = max(score_lst[i][j], score_lst[i][jj])
            max_score_lst.append(max_two_song)
    return max_score_lst

all_max_score_lst =  []
for i in range(int(n)):
    all_max_score_lst.append(getMaxScoreList(score_lst[0],n,m))

total = 0
for i in range(len(all_max_score_lst[0])):
    sum_in_cols = 0
    for j in range(int(n)):
        sum_in_cols+= all_max_score_lst[j][i]
    if total <= sum_in_cols:
        total = sum_in_cols
print(total)