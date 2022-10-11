""":01
重複無しで３つの数を選びそれらの合計が x となる組み合わせの数
"""

while True:
    n,s = input().split()
    if n==0:
        break
    # 全探索する
    lst =[i for i in range(1,n+1)]
    for i in lst:
        for j in range(n-1):
            for k in range(n-2):
for i in range()