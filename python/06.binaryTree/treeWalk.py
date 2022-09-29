'''Binary Tree Walk(木の巡回)
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
-------
Output
Preorder
 0 1 2 3 4 5 6 7 8
Inorder
 2 1 3 0 6 5 7 4 8
Postorder
 2 3 1 6 7 5 8 4 0
'''


class Node:
    def __init__(self,parent,left,right):
        self.parent = parent
        self.left = left
        self.right = right

def preorder(vid):
    print(f' {vid}', end="")
    if node[vid].left == -1 and node[vid].right == -1:
        return
    if node[vid].left != -1:
        preorder(node[vid].left)
    if node[vid].right != -1:
        preorder(node[vid].right)


def interorder(vid):
    if vid == None:
        return
    if node[vid].left != -1:
        interorder(node[vid].left)
    print(f' {vid}',end="")
    if node[vid].right != -1:
        interorder(node[vid].right)


def postoder(vid):
    if vid == None:
        return
    if node[vid].left != -1:
        postoder(node[vid].left)
    if node[vid].right != -1:
        postoder(node[vid].right)
    print(f' {vid}',end="")

if __name__=="__main__":
    n = int(input())
    node = []
    pre = [None]*n
    
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

    # RootはVID=0とは限らないので、Rootを特定する(重要!)
    for id in range(n):
        if node[id].parent == -1:
            root_vid = id
            break
    
    # node= [node,node,node....]
    print("Preorder")
    preorder(root_vid)
    print("")
    print('Inorder')
    interorder(root_vid)
    print("")
    print('Postorder')
    postoder(root_vid)
    print("")