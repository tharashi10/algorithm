'''Treeの再構築
PreOrder と InOrderから部分木を作って再起的に二分木を構築する
方針:
1.PreOrderから根Nodeを発見する
2.発見したNodeに対して、InOrderを左部分木と右部分木に分ける
3.左部分木と、右部分木でPreOrderを作成する
4.作成したPreOrderと部分木をInputにして、1.の手番を始める(再帰)
----
Input
5
1 2 3 4 5
3 2 4 1 5
--
Output
3 4 2 5 1
'''


class Node:
    def __init__(self,parent,left,right):
        self.parent = parent
        self.left = left
        self.right = right

def reconst(subtree_pre,subtree_in):
    if len(subtree_pre)==0 or len(subtree_in)==0:
        return
    root = subtree_pre[0]
    mid = subtree_in.index(root)
    if mid > 0:
        node[root].left = subtree_pre[1:mid+1][0]
        node[subtree_pre[1:mid+1][0]].parent = root
    if mid+1 < len(subtree_pre):
        node[root].right = subtree_pre[mid+1:][0]
        node[subtree_pre[mid+1:][0]].parent = root
    
    reconst(subtree_pre[1:mid+1], subtree_in[:mid])
    reconst(subtree_pre[mid+1:], subtree_in[mid + 1:])

def postoder(vid):
    if vid == None:
        return
    if node[vid].left != -1:
        postoder(node[vid].left)
    if node[vid].right != -1:
        postoder(node[vid].right)
    post.append(vid)

if __name__ == "__main__":
    n = int(input())
    pre_order = list(map(int,input().split()))
    in_order = list(map(int,input().split()))
    
    node = []
    post = []
    # Initiation
    for i in range(n+1):
        if i==0:
            node.append(Node(None,None,None))
        else:
            node.append(Node(-1,-1,-1))
    
    # Reconstruct:二分木
    reconst(pre_order,in_order)

    # RootはVID=0とは限らないので、Rootを特定する(重要!)
    for id in range(1,n+1):
        if node[id].parent == -1:
            root_vid = id
            break
    
    postoder(root_vid)
    print(" ".join(map(str, post)))
    