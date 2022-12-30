"""
6
0 1 2 3 4 5
"""

def main():
    N = int(input())
    A = list(map(int,input().split()))
    ll = [0,0,0]
    MOD = int(1e9)+7

    ans = 1
    for a in A:
        ans*=ll.count(a)
        for i in range(len(ll)):
            if a==ll[i]:
                ll[i]+=1
                break
    print(ans%MOD)

if __name__=="__main__":
    main()
