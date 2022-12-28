"""
2 50
6 10
"""

import functools
import math
def main():
    N, M = map(int,input().split())
    ll = list(map(int,input().split()))
    
    def lcm(nums):
        return functools.reduce(math.lcm,nums)
    
    ll = list(map(lambda x: x//2, ll))
    mi = lcm(ll)
    ans = 0
    
    tmp = 0
    while (tmp<M):

    for k in range(1,n,2):
        tmp = k*mi
        if :
            break
        ans+=1

    print(ans)

if __name__ == "__main__":
    main()
