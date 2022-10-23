"""
Binary Search
・方針: Midを見つけていく
・注意: 21行目のrightのIndex -1いらない
・注意: 28行目の x が大きすぎてList外となるケースを弾くようにしたほうがいい
(x<listだとACしなかった)

In
5
1 2 3 4 5
3
3 4 1
Out
3
"""

n = int(input())
trg = list(map(int,input().split()))
m = int(input())
src = list(map(int,input().split()))

def search(lst, x):
    left = 0
    right = len(lst)
    while left<right:
        mid=(left+right)//2
        if lst[mid]==x:
            return mid
        elif x > lst[mid]:
            left = mid+1
        else:
            right=mid
    return -1

cnt = 0
for i in range(len(src)):
    v = search(trg,src[i])
    if v==-1:
        continue
    else:
        cnt+=1
print(cnt)