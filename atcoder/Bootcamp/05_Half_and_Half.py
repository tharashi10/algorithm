""":
C - Half and Half
In:  1500 2000 1600 3 2
Out: 7900
-----
実行時間: 23 ms
*15分で解けた。けど全探索してないから模範解答見ておくべし
"""

a,b,c,x,y = map(int,input().split())
set_cnt = 0

def buyBySet(a,b,c,x,y):
    if x>=y:
        set_cnt = y
        x,y = x-y,y-y
    else:
        set_cnt=x
        x,y = x-x,y-x
    return set_cnt*c*2 + a*x + b*y

def buyBySetOver(a,b,c,x,y):
    if x>=y:
        set_cnt = x
        #x,y = x-y,y-y
    else:
        set_cnt=y
        #x,y = x-x,y-x
    return set_cnt*c*2

def buyByEach(a,b,c,x,y):
    return a*x + b*y

print(min(buyByEach(a,b,c,x,y),buyBySetOver(a,b,c,x,y),buyBySet(a,b,c,x,y)))
