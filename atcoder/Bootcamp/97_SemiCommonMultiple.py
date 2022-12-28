"""
ロジックあってる
PythonだとREする
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
    com = lcm(ll)
    ans = (M//com+1)//2 # Mまでに最小公倍数が何個あるのかを算出(但し奇数を算出)
    print(ans)

if __name__ == "__main__":
    main()
