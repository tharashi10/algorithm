'''最大公約数
Euclid使うと速い: 0.01s(約500倍速くなった)
'''
x,y = map(int, input().split())

def euclid(x,y):
    if x<y:
        # swap
        x,y = y,x
    while(y>0):
        # remainder
        r = x%y
        x = y
        y = r
    return x

print(euclid(x,y))

'''TLEとなったコード 
812500000 1000000000のケースでNG :4.99s
x,y = map(int, input().split())

def gcd(k,l):
    t = min(k,l)
    for t in reversed(range(1,t+1)):
        if k%t == 0 and l%t == 0:
            return t
            break
        else:
            continue

print(gcd(x,y))'''