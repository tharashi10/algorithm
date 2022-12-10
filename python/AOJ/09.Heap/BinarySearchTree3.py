"""
BinarySearchTree;二分探索木
Input()
-------
18
insert 8
insert 2
insert 3
insert 7
insert 22
insert 1
find 1
find 2
find 3
find 4
find 5
find 6
find 7
find 8
print
delete 3
delete 7
print
-------
yes
yes
yes
no
no
no
yes
yes
 1 2 3 7 8 22
 8 2 1 3 7 22
 1 2 8 22
 8 2 1 22
"""


class Node:
    def __init__(self,key,right,left):
        self.key = key
        self.right = right
        self.left = left


def insert(key):
    global root  # Noneである可能性あり
    if root:
        child = root
        while child:
            if key < child.key:
                parent = child
                child = child.left
            else:
                parent = child
                child = child.right
        # この時点で末端まできている
        if key < parent.key:
            parent.left = Node(key,None,None)
        else:
            parent.right = Node(key,None,None)
    else:
        # rootが存在しない場合
        root = Node(key,None,None)

def walktree(node,order):
    walked = ""
    if node:
        if order=="Pre":
            walked += f' {node.key}'
        walked += walktree(node.left,order)
        if order=="In":
            walked += f' {node.key}'
        walked += walktree(node.right,order)
    #print(walked)
    return walked

def prints():
    print(walktree(root,"In"))
    print(walktree(root,"Pre"))

def delete(key):
    global root
    parent, node= None, root
    while node.key != key:
        parent, node = node, node.left if key < node.key else node.right
    # 子が右/左いる場合
    if node.left and node.right:
        parent, to_delete = node, node.right
        while to_delete.left:
            parent, to_delete = to_delete, to_delete.left
        node.key = to_delete.key
    else:
        to_delete = node

    child = to_delete.left or to_delete.right
    if not parent:
        root = child
    elif parent.left == to_delete:
        parent.left = child
    else:
        parent.right = child

def find(key):
    node = root
    while node and node.key != key:
        node = node.left if key < node.key else node.right
    print("yes" if node else "no")

if __name__ == "__main__":
    root = None
    # REPL
    # Key:標準入力でくる命令 | Value:メソッド
    cmds = {"print":prints, "insert":insert, "find":find, "delete":delete}
    for i in range(int(input())):
        cmd_name, *key = input().split()
        # cmds[cmd_name] = <function __main__.insert()>
        # map(int,key) = [<map at 0x1076f6980>]
        cmds[cmd_name](*map(int,key))
