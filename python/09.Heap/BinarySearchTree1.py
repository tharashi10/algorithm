"""
BinarySearchTree;二分探索木
Input()
-------
8
insert 30
insert 88
insert 12
insert 1
insert 20
insert 17
insert 25
print
-------
 1 12 17 20 25 30 88
 30 12 1 20 17 25 88
""""

class Node:
    def __init__(self,key,parent,right,left):
        self.key = key
        self.parent = parent
        self.right = right
        self.left = left

def insert(Tree, num):
    y = None # y: numと比較するやつ
    x = Tree[0] #root

    # rootがあればぐるぐる
    while x != Node(-1,-1,-1,-1):
        y = x
        if num.key < y.key:
            x = x.left
        else:
            x = x.right
    
    num.parent = y # num : Node(key,parent,right,left)
                   # ex  : Node(23,y,-1,-1)  

    # Treeが空かどうかで分岐
    if y == Node(-1,-1,-1,-1):
        Tree[0] = z
    elif num.key < y.key:
        y.left = num
    else:
        y.right = num


def print():
    return None


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


if __name__ == "__main__":
    n = input()
    node = []

    # init
    for i in range(n):
        node.append(Node(-1,-1,-1))
    
    for i in range(n):
        s = str(input())
        if s.startwith("insert"):
            insert(node, s[7:])
        else:
            print()
