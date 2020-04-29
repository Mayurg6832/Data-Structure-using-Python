class Node:
    def __init__(self,data):
        self.value=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
        
    def insertAtEnd(self,data):
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
linkedlist.insertAtEnd(15)
linkedlist.insertAtEnd(25)
linkedlist.insertAtEnd(35)

linkedlist.display()
