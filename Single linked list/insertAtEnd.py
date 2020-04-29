class Node:
    def __init__(self,data):
        self.value=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None

    def insertNode(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
        else:
            current=self.head
            while True:
                if current.next==None:
                    break
                current=current.next
            current.next=node

    def insertAtBegi(self,data):
        node=Node(data)
        if self.head==None:
            self.head=node
        else:
            temp=self.head
            self.head=node
            self.head.next=temp

    def display(self):
        if self.head==None:
            print("Nothing")
        else:
            current=self.head
            while True:
                if current==None:
                    break
                print(current.value)
                current=current.next

linkedlist=linkedList()
linkedlist.insertNode(3)
linkedlist.insertNode(1)
linkedlist.insertNode(4)
linkedlist.insertNode(5)
linkedlist.insertAtBegi(0)

linkedlist.display()
