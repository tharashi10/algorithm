# Template
## 標準入力系
- 横並び数字
```:python
10
8 5 9 2 6 3 7 1 10 4
--------------------
N = input()
A = list(map(int,input().split())) 
```

- 縦並び数字
```:python
5 
5
1
4
3
2
--------------------
N = int(input())
A = [int(input()) for _ in range(N)]
```

- ２個並び(文字・数字混合)
```:python
5 100
p1 150
p2 80
p3 200
p4 350
p5 20
--------------
n,t = map(int,input().split())
queue = [[]]* m
    for i in range(n):
        a,b = input().split()
        queue[i] = [a,int(b)]
```

- 改行コードを取り除く
```:python
2 
insert 1000000000
insert 999999999
------------
for _ in range(int(input())):
    command = input().rstrip()
```

- 迷路
```:python
7 8  # 行数R/ 列数C
2 2  # Start sy,sx
4 5  # Goal  gy,gx
########
#......#
#.######
#..#...#
#..##..#
##.....#
########
----------
R, C = map(int,input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
visitedList = [[None]*C for _ in range(R)]
maze = [input() for i in range(R)]
```

## キューの扱い
### Collections
- deque
```:python
from collections import deque
queue = deque([[sy,sx]])
y, x = queue.popleft() #先頭
y, x = queue.pop() 　　#最後
y, x = queue.append() #追加
```

- namedTuple(簡単に immutable なクラスを定義)
```:python
from collections import namedtuple
Human = namedtuple('Oracle',('name','age')) #(クラス名, (属性名))
He = Human("Hoge",36)
print(He.age)
print(*He)
```

