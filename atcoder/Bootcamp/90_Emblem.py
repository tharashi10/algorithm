"""
Emblem
簡単
0 2
6 3
2 4
"""
import math
def main():
    N,M = map(int,input().split())
    
    rr = []
    for _ in range(N): # radius
        x,y,r = map(int,input().split())
        rr.append((x,y,r))
    
    ll = []
    for _ in range(M): # without/radius
        x,y = map(int,input().split())
        ll.append((x,y))
    
    rad = float(1e6)
    # Case1
    for i in range(len(rr)):
        for j in range(len(ll)):
            d = math.sqrt((rr[i][0]-ll[j][0])**2 + (rr[i][1]-ll[j][1])**2)
            tmp = d-rr[i][2]
            if tmp >0:
                rad = min(rad,tmp)
    
    # Case2
    for i in range(len(ll)-1):
        for j in range(i+1,len(ll)):
            d = math.sqrt((ll[i][0]-ll[j][0])**2 + (ll[i][1]-ll[j][1])**2)
            tmp = d/2
            if tmp >0:
                rad = min(rad,d/2)
    
    # Case3
    for i in range(len(rr)-1):
        for j in range(i+1,len(rr)):
            d = math.sqrt((rr[i][0]-rr[j][0])**2 + (rr[i][1]-rr[j][1])**2)
            if d > rr[i][2]+rr[j][2]:
                rad = min(rad,min(rr[i][2],rr[j][2]))

    print(rad)

if __name__=="__main__":
    main()
