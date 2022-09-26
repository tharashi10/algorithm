'''二分木(Binary Tree)
Nodeに対して、
Parent, Left, Rightを決める
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


def set_depth(vid,d):
    depth_list[vid] = d
    if (node[vid].left == -1 and node[vid].right == -1):
        return
    if (node[vid].left != -1):
        set_depth(node[vid].left,d+1)
    if (node[vid].right != -1):
        set_depth(node[vid].right,d+1)

def set_height(vid,h):
    if (node[vid].left == -1 and node[vid].right == -1):
        return
    if (node[vid].left != None):
        set_height(node[vid].left,d+1)
    if (node.right != None):
        set_height(node[vid].right,d+1)

def get_siblings(vid):
    # 自身がLeftだった場合
    if node[node[vid].parent].right != node[vid] and node[node[vid].parent].right != -1:
        return node[node[idx].parent].right
    # 自身がRightだった場合
    if node[node[vid].parent].left != node[vid] and node[node[vid].parent].left != -1:
        return node[node[vid].parent].left

    return None


def print_output():
    print(node)
    print(depth_list)

if __name__ == "__main__":
    n = int(input())
    node = []
    depth_list = [None]*n
    
    for i in range(n):
        node.append(Node(-1,-1,-1))
    
    # InputからNode を作る工程
    for j in range(n):
        vid,l,r = map(int,input().split())
        node[vid].left = l
        node[vid].right = r
        if node[vid].left != -1:
            node[l].parant = vid
        if node[vid].right != -1:
            node[r].parant = vid

    set_depth(0,0)
    for k in range(n):
        print(get_siblings(k))
    
    print_output()
