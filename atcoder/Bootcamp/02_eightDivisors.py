""":02
Now, your task is this: how many odd numbers 
with exactly eight positive divisors are there between 1 and N (inclusive)?
In: 105
Out: 1
実行速度:25 ms
"""

n = int(input())
all_lst = [i for i in range(1,n+1)] 
odd_lst = list(filter(lambda x: x%2==1 ,all_lst))

def hasEightDevisor(x):
    div_lst = []
    for i in [i for i in range(1,n+1)]:
        if x%i==0:
            div_lst.append(i)
    if len(div_lst)==8:
        return True
    else:
        return False

cnt = 0
for k in odd_lst:
    if hasEightDevisor(k):
        cnt+=1

print(cnt)
