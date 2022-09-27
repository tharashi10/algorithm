'''二分木(Binary Tree)
Nodeに対して、
Parent, Left, Rightを決める
→この情報から、再帰を使って高さ・深さ・次数・Nodeタイプを判別する
--
Input
9
0 1 4
1 2 3
2 -1 -1
3 -1 -1
4 5 8
5 6 7
6 -1 -1
7 -1 -1
8 -1 -1
------
Output
node 0: parent = -1, sibling = -1, degree = 2, depth = 0, height = 3, root
node 1: parent = 0, sibling = 4, degree = 2, depth = 1, height = 1, internal node
node 2: parent = 1, sibling = 3, degree = 0, depth = 2, height = 0, leaf
node 3: parent = 1, sibling = 2, degree = 0, depth = 2, height = 0, leaf
node 4: parent = 0, sibling = 1, degree = 2, depth = 1, height = 2, internal node
node 5: parent = 4, sibling = 8, degree = 2, depth = 2, height = 1, internal node
node 6: parent = 5, sibling = 7, degree = 0, depth = 3, height = 0, leaf
node 7: parent = 5, sibling = 6, degree = 0, depth = 3, height = 0, leaf
node 8: parent = 4, sibling = 5, degree = 0, depth = 2, height = 0, leaf
'''


# 構造体の変数はIndex
class Node:
    def __init__(self,parent,left,right):
        self.parent = parent
        self.left = left
        self.right = right

# 深さを設定する
def set_depth(vid,d):
    depth_list[vid] = d
    if node[vid].left == -1 and node[vid].right == -1:
        return
    
    if (node[vid].left != -1):
        set_depth(node[vid].left,d+1)
    if (node[vid].right != -1):
        set_depth(node[vid].right,d+1)

# Heightを設定する
def set_height(vid):
    h1=0
    h2=0
    if (node[vid].left != -1):
        h1 = set_height(node[vid].left) + 1
    if (node[vid].right != -1):
        h2 = set_height(node[vid].right) + 1
    height_list[vid] = max(h1,h2)
    return height_list[vid]


def get_siblings(vid):
    # 根の場合
    if node[vid].parent == -1 :
        return -1
    
    # 自身がRightだった場合
    if node[node[vid].parent].right == vid:
        return node[node[vid].parent].left
    
    # 自身がLeftだった場合
    if node[node[vid].parent].left == vid:
        return node[node[vid].parent].right


if __name__ == "__main__":
    n = int(input())
    node = []
    depth_list = [None]*n
    height_list = [None]*n
    
    # 初期化
    for i in range(n):
        node.append(Node(-1,-1,-1))
    
    # Input から Node を作る工程
    for j in range(n):
        vid,l,r = map(int,input().split())
        node[vid].left = l
        node[vid].right = r
        if l != -1:
            node[l].parent = vid
        if r != -1:
            node[r].parent = vid

    # RootはVID=0とは限らないので、Rootを特定する
    for id in range(n):
        if node[id].parent == -1:
            root_vid = id
            break
    set_depth(root_vid,0)
    set_height(root_vid)
    for id in range(n):
        s = get_siblings(id)

        # NodeType
        if node[id].parent == -1:
             node_type = "root"
        elif node[id].right == node[id].left == -1:
            node_type = "leaf"
        else:
            node_type = "internal node"

        # Degree
        if node[id].right == node[id].left == -1:
             d = 0
        elif node[id].right >= 0 and node[id].left >= 0:
            d = 2
        else:
            d = 1 
        print(f'node {id}: parent = {node[id].parent}, sibling = {s}, degree = {d}, depth = {depth_list[id]}, height = {height_list[id]}, {node_type}')
