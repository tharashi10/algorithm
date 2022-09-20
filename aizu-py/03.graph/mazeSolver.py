""":
迷路問題をDFSを使って解く
今回は再帰を利用する
また、座標はCollectionを使っている
"""

from collections import namedtuple
def search_maze(maze, s, e):
    def maze_helper(cur):
        print(cur.x,cur.y)
        print(maze[s.x][s.y])
        if not (0 <= cur.x < len(maze) and
                0 <= cur.y < len(maze[cur.x]) and
                maze[cur.x][cur.y]==0): # 0:White, 1:Black
                return False
        path.append(cur) # Pathとなり得るので追加
        maze[cur.x][cur.y] = 1
        if cur == e:
            print("goal")
            return True # ゴールならこれ以降のCodeは実行せず関数を終了させる

        if any(map(maze_helper,(Coordinate(cur.x - 1, cur.y),
                                Coordinate(cur.x + 1, cur.y),
                                Coordinate(cur.x, cur.y - 1),
                                Coordinate(cur.x, cur.y + 1)))):
            return True # Trueが返る→どれかでゴールに辿り着いている

        del path[-1] # 道がなければAppendしたCurをPopさせる
        return False
    
    path = []
    if not maze_helper(s):
        return [] # No Pathway
    print(path)
    return path

if __name__=="__main__":
    #maze = [
    #    [1,0,0,0,0,0,1,1,0,1],
    #    [0,0,1,0,0,0,1,1,0,1],
    #    [1,0,1,0,0,1,1,0,1,1],
    #    [0,0,0,1,1,1,0,0,1,0],
    #    [0,1,1,0,0,0,1,1,0,1],
    #    [0,1,1,0,0,1,0,1,1,0],
    #    [0,0,0,0,1,0,0,0,0,0],
    #    [1,0,1,0,1,0,1,0,0,0],
    #    [1,0,1,1,0,0,0,1,1,1],
    #    [1,0,0,0,0,0,0,1,1,0]
    #]
    maze = [
        [1,0,0,0,0],
        [1,0,0,1,1],
        [1,0,1,1,0],
        [0,0,1,0,0],
        [0,0,0,1,0]
    ]
    Coordinate = namedtuple('xyZahyou',('x','y'))
    s = Coordinate(4,0)
    e = Coordinate(0,4)
    search_maze(maze, s, e)
    # [xyZahyou(x=4, y=0), xyZahyou(x=3, y=0), xyZahyou(x=3, y=1), xyZahyou(x=2, y=1), xyZahyou(x=1, y=1), xyZahyou(x=0, y=1), xyZahyou(x=0, y=2), xyZahyou(x=0, y=3), xyZahyou(x=0, y=4)]