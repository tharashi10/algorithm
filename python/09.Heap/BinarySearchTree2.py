"""
BinarySearchTree;二分探索木
Input()
-------
10
insert 30
insert 88
insert 12
insert 1
insert 20
find 12
insert 17
insert 25
find 16
print
-------
yes
no
 1 12 17 20 25 30 88
 30 12 1 20 17 25 88
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

def delete():
    return None

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
