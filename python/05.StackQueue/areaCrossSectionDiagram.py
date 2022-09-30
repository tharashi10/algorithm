"""
Stackを使う問題
水たまりの面積を求める
Input
\\//
---
Output
4
1 4
--
Input
\\///\_/\/\\\\/_/\\///__\\\_\\/_\/_/\
---
35
5 4 2 1 19 9
"""
from collections import deque


def calc(st):
    stack1 = deque()
    stack2 = deque([])
    #print("---st----")

    for i, ch in enumerate(st):
        if ch == '\\':
            stack1.append(i)
        elif ch == '/' and stack1:
            pop = stack1.pop() # X座標
            delta = i - pop # X座標の差分

            #idx : Stack2のLastのIndex
            # 前回計算した面積が、今回計算する範囲(idx < X < i)に収まっている場合、面積を増加する
            while stack2 and stack2[-1][0] > pop:
                delta +=stack2.pop()[1]
            stack2.append([i,delta])

    return stack2

if __name__=="__main__":
    st = input()
    area_list = []
    stack2 = calc(st)
    for i in range(len(stack2)):
        area_list.append(stack2[i][1])
    
    print(sum(area_list))
    area_list.insert(0, len(area_list))
    print(' '.join(map(str,area_list)))
