class Node:
    def __init__(self,data):
        self.value=data
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None

    def insertAtBegining(self,data):
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
linkedlist.insertAtBegining(10)
linkedlist.insertAtBegining(20)
linkedlist.insertAtBegining(30)

linkedlist.display()
