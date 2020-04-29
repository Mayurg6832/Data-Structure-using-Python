class Node:
    def __init__(self,data):
        self.value=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
        
        
    def insertAtPosition(self,data,position):
        node=Node(data)
        pos=1
        if position == 0:
            temp=self.head
            self.head=node
            node.next=temp
            return
        if self.head==None:
            self.head=node
        else:
            current=self.head
            while True:
                if pos==position:
                    break
                current=current.next
                pos+=1
            #1->2->3->4
            temp=current.next
            current.next=node
            node.next=temp
            
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

linkedlist.insertAtPosition(1,0)
linkedlist.insertAtPosition(2,1)
linkedlist.insertAtPosition(3,2)
linkedlist.insertAtPosition(4,3)
linkedlist.insertAtPosition(5,2)
linkedlist.display()
