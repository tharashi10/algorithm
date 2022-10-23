"""
Eight Queens Problems
・方針: 8!の順列を探索する
・例えば,(6, 0, 2, 7, 5, 3, 1, 4)とあったときに、
(0行目のQueenの配置列,1行目のQueenの配置列,2行目のQueenの配置列,3行目のQueenの配置列..)
と定義できる。なぜなら、縦横は攻撃範囲になるため同じ行および列にQueenが配置されることはないため。
・斜め判定は、サクッといかないので要熟考
→1次関数的に考える: [x+y が同じ] または [x-y が同じ]場合は、対角線上に乗ってしまうことを利用する

Input---
2
2 2
5 3
Output---
......Q.
Q.......
..Q.....
.......Q
.....Q..
...Q....
.Q......
....Q...
"""
import itertools

n = int(input())
q = []
for _ in range(n):
    q.append(list(map(int,input().split())))

patterns = list(itertools.permutations(range(8)))

for p in patterns:
    #斜め判定
    xy = []
    for i in range(len(p)):
        xy.append(i+p[i])
    
    xy_ = []
    for i in range(len(p)):
        xy_.append(i-p[i])
    
    if len(set(xy)) !=8 or len(set(xy_))!=8:
        continue
    
    cnt_judge = 0
    for j in range(len(q)):
        if p[q[j][0]]!=q[j][1]:
            cnt_judge+=1

    if cnt_judge ==0:
        #print(f"p : {p}") #(7, 6, 2, 5, 4, 3, 1, 0)
        
        for i in range(8):
            l = ['.' if n!=p[i] else 'Q' for n in range(8)]
            print("".join(map(str,l)))
