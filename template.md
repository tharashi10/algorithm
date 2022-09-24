# Template
## 標準入力系
#### 横並び数字
```py
'''
10
8 5 9 2 6 3 7 1 10 4
'''
N = input()
A = list(map(int,input().split())) 
```

#### 縦並び数字
```py
'''
5 
5
1
4
3
2
'''
N = int(input())
A = [int(input()) for _ in range(N)]
```

#### ２個並び(文字・数字混合)
```py
'''
5 100
p1 150
p2 80
p3 200
p4 350
p5 20
'''
n,t = map(int,input().split())
queue = [[]]* m
    for i in range(n):
        a,b = input().split()
        queue[i] = [a,int(b)]
```

#### 改行コードを取り除く
```py
'''
2 
insert 1000000000
insert 999999999
'''
for _ in range(int(input())):
    command = input().rstrip()
```

#### 迷路
```py
'''
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
'''
R, C = map(int,input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
visitedList = [[None]*C for _ in range(R)]
maze = [input() for i in range(R)]
```

#### トランプの入力

```py
'''
6
D 3
H 2
D 1
S 3
D 2
C 1
'''
A = [[kind,int(num)] for kind,num in (list(input().split()) for _ in range(0,n))]
```

## 標準出力系
#### 「文字 数字」で出力する
```py
while i<n:
    print("%s %s" %(A[i][0],A[i][1]))
    i+=1
```
----

## キューの扱い
#### Collections
- deque
```py
from collections import deque
queue = deque([[sy,sx]])
y, x = queue.popleft() #先頭
y, x = queue.pop() 　　#最後
y, x = queue.append() #追加
```

## 構造体の扱い
#### Collections
- namedTuple(簡単に immutable なクラスを定義)
```py
from collections import namedtuple
Human = namedtuple('Oracle',('name','age')) #(クラス名, (属性名))
He = Human("Hoge",36)
print(He.age)
print(*He)
```

## 辞書やリストをソートしたい場合
- lambdaを使う
```py
l_stable = sorted(l, key=lambda x:x[1])
```

## リストの重複をなくしてUniqueにしたい場合
- Setを使う(setは数学的な集合を表現するCollectionと覚えておく)
- そのため、重複要素は排除される。また論理演算(& や | など)も自在
```py
A_list = [1, 2, 3]
B_list = [1, 2, 4]
s_AB = set(A_list + B_list)
list(s_AB)
```