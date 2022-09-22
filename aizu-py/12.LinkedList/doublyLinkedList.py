"""
双方向連結リスト
Input()
7
insert 5
insert 2
insert 3
insert 1
delete 3
insert 6
delete 5
-------
Output()
6 1 2

---
Inpute (2)
9
insert 5
insert 2
insert 3
insert 1
delete 3
insert 6
delete 5
deleteFirst
deleteLast
--
Input : TODO
8
insert 1000000000
insert 999999999
deleteLast
insert 1234566890
insert 5
deleteFirst
insert 7
delete 5
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.start = Node(None)
        self.start.prev = self.start
        self.start.next = self.start

    def insertNodeAtFirst(self, x):
        newNode = Node(x)
        newNode.prev = self.start
        newNode.next = self.start.next
        self.start.next = newNode
        self.start.next.prev = newNode
        #print("-----")
        #print(newNode.prev)
        #print(newNode.next)

    def deleteAtFirst(self):
        delNode = self.start.next
        if delNode == self.start:
            print("The linked list empty. Cannot delete an element.")
            return
        else:
            if delNode.next != self.start:
                self.start.next = delNode.next
                delNode.next.prev = self.start
            else:
                self.start.next = self.start

    def listSearch(self, x):
        current = self.start.next
        while current != self.start and current.data != x:
            current = current.next
        return current

    def deleteNode(self, node):
        if node == self.start:
            return
        print("---deleteNode--")
        print(node.prev)
        node.prev.next = node.next
        node.next.prev = node.prev

    def deleteNodeByData(self, x):
        self.deleteNode(self.listSearch(x))

    def deleteLast(self):
        current = self.start.next
        if current == self.start:
            print("The linked list empty. Cannot delete an element.")
            return
        
        else:
            while current.next != self.start:
                current = current.next
            print('---deleteLast---')
            #self.deleteNode(current)
            current.prev.next = self.start

            #[TODO]
    
    def printNode(self):
        current = self.start.next
        while current != self.start:
            if current.next is not self.start:
                print(current.data, end=" ")
            else:
                print(current.data)
            current = current.next

if __name__=="__main__":
    linkedList = LinkedList()

    for _ in range(int(input())):
        # 引数の個数が可変なので文字連結しちゃう
        # command, s = (input().split())

        # rstrip()で改行コードを取り除く
        command = input().rstrip()
        #print(command)
        if command[0] == "i":
            linkedList.insertNodeAtFirst(int(command[7:]))
        elif command[6] == "F":
            linkedList.deleteAtFirst()
        elif command[6] == "L":
            linkedList.deleteLast()
        else :
            #command == "deleteFirst":
            linkedList.deleteNode(int(command[7:]))
            
    linkedList.printNode()