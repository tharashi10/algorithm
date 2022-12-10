""":
お釣りの最小枚数(貪欲法)
・その場その場で最適解を選び続ける方法
・以下のやり方では特にDP的な解き方はしていない
Input
100
Output
4
"""

while True:
    num = int(input())
    if num == 0:
        break
    coins = [25,10,5,1]
    tmp = num
    result = 0
    for i in range(0,len(coins)):
        if tmp == 0:
            break
        result += tmp//coins[i]
        tmp = tmp%coins[i]
    print(result)
    break
