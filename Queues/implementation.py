class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
    
    def enqueue(self,data):
        node=Node(data)
        if self.front==None:
            self.front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node
    def peek(self):
        if self.front==None:
            print("Empty Queue")
        else:
            print(self.front.data)
    def dequeue(self):
        if self.front==None:
            return print("Empty Queue")
        if self.front==self.rear:
            self.rear=None
        self.front=self.front.next

queue=Queue()
queue.enqueue("hello")
queue.peek()
queue.enqueue("world")
queue.peek()
queue.dequeue()
queue.peek()
queue.dequeue()
queue.peek()