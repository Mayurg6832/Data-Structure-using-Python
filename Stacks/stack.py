class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
        self.botton=None
    
    def push(self,data):
        node=Node(data)
        if self.top==None:
            self.top=node
        else:
            current=self.top
            self.top=node
            self.top.next=current
    def peek(self):
        if self.top==None:
            print("Empty Stack")
        else:
            print(self.top.data)
    def pop(self):
        if self.top==None:
            print("Empty Stack")
        else:
            temp=self.top
            self.top=self.top.next
            del temp

stack=Stack()
stack.push("hello")
stack.peek()
stack.push("World")
stack.peek()
stack.push("123")
stack.peek()
stack.pop()
stack.peek()
stack.pop()
stack.peek()
stack.pop()
stack.peek()