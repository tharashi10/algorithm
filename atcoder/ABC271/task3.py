"""ABC271
漫画を連続で読むために本をどう買うかの問題(C)
Input
6
1 2 4 6 7 271
4
"""

n = int(input())
l = list(map(int,input().split()))

def should_sell(L):
    maxNum = max(L)
    L.remove(maxNum)
    nextMaxNum = max(L)
    return maxNum, nextMaxNum

mm = [0]
cnt = 0
if min(l) == 1:
    l.pop(l.index(1))
    mm.append(1)
    cnt=1

while len(l) >=2:
    tmp = max(mm)+1
    if tmp in l:
        l.pop(l.index(tmp))
        #mm.append(tmp)
        cnt +=1
    else:
        rm = should_sell(l)
        #l.remove(rm[0])
        l.remove(rm[1])
        l.append(tmp)

out = len(mm[1:])
print(cnt)
