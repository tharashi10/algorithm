""":最古の遺跡
日本情報オリンピック本選考
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
    point_list.append(tuple(map(int,input().split())))

# in zip()は使うな.くそ遅い.TLEにならない
# setで、removeは使うな. 引数Checkのハンドリングめんどい
for i in range(n-1):
    for j in range(i+1,n):
        ll = set(point_list)
        p1 = (point_list[i][0],point_list[i][1])
        p2 = (point_list[j][0],point_list[j][1])
        vec = (p2[0]-p1[0],p2[1]-p1[1]) 
        vertical = (-vec[1],vec[0])
        
        #ll = list(filter(lambda x: x not in [p1,p2], point_list))
        ll.discard(p1)
        ll.discard(p2) # setでは discard 使える
        p1_ = (p1[0]+vertical[0],p1[1]+vertical[1])
        p2_ = (p2[0]+vertical[0],p2[1]+vertical[1])

        if (p1_) in ll and (p2_) in ll:
            tmp = vec[0]*vec[0] + vec[1]*vec[1]
            if square < tmp:
                square=tmp

print(square)
