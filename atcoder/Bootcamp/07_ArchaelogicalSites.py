"""
10
9 4
4 3
1 1
4 2
2 4
5 8
4 0
5 3
0 5
5 2
"""

n = int(input())
point_list = []
square = 0

for i in range(n):
    point_list.append(list(map(int,input().split())))

for i in range(n-1):
    for j in range(i+1,n):
        p1 = [point_list[i][0],point_list[i][1]]
        p2 = [point_list[j][0],point_list[j][1]]
        
        vec = [y-x for x,y in zip(p1,p2)]
        vec_vertical = [-vec[1],vec[0]]
        p1_ = [x+y for x,y in zip(vec_vertical, p1)]
        p2_ = [x+y for x,y in zip(vec_vertical, p2)]
        
        ll = list(filter(lambda x: x not in [p1,p2], point_list))
        if p1_ in ll and p2_ in ll:
            tmp = sum([i**2 for i in vec])
            if square < tmp:
                square=tmp
print(square)
