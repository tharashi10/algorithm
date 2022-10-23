"""
B - Buildings are Colorful!
(全探索bitのカテゴリにある)
・純粋にFor文とIF分岐でやると、5つくらい正解になる(課題1クリア)
・ポイントは「高さを 1 増やすごとに 1 円かかります」でコストを最小とする必要あり
・[方針]見えるべき建物について全探索する(Bit)

Input
-----
5 5
3949 3774 3598 3469 3424
Output
-----
1541
"""

n,k = map(int,input().split())
l = list(map(int, input().split()))

# これを10**8でやってて沼った（テストケースは大きめのものが使われていた模様）
min_cost = 10**20
for i in range(2**n):
    cnt = 0
    for jj in range(n):
        if (i>>jj)&1:
            cnt+=1
    if cnt!=k:
        continue

    score = 0
    max_h = l[0]
    for j in range(n):
        if (i>>j)&1:
            if l[j] <= max_h:
                score+=(max_h-l[j])
                max_h+=1
            else:
                max_h=(l[j]+1)
        else:
            max_h = max(max_h,l[j]+1)
    
    min_cost = min(min_cost,score)
    #print(f"i = {i} : score :{score}")

print(min_cost)
