"""
Binary Search
・方針: Midを見つけていく
In
5
1 2 3 4 5
3
3 4 1
Out
3
"""

n = int(input())
s = list(map(int,input().split()))
m = int(input())
t = list(map(int,input().split()))

def search(lst, x):
    left = lst[0]
    right = lst[len(lst)-1]

    while left<=right:
        mid=(left+right)//2
        if lst[mid]==x:
            return mid
        elif x < lst[mid]:
            right=mid
        else:
            left=mid
    return -1

for i in range(m):
    v = search(s,t[i])
    if v==-1:
        print("No")
    else:
        print("Yes")
