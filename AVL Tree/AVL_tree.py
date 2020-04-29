class Node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
        self.level=1

class Tree:
    def __init__(self):
        self.head=None
    
    def insert(self,node):
        if self.head==None:
            self.head=node

        else:
            currentNode=self.head
            while True:
                if currentNode.val<node.val:
                    if currentNode.right is None:
                        currentNode.right=node
                        break
                    currentNode=currentNode.right
                else:
                    if currentNode.left is None:
                        currentNode.left=node
                        break
                    currentNode=currentNode.left
        
        self.level=self.depth(self.head)
        balance_level=self.balance(self.head)

        if balance_level>1 and node.val<self.head.left.val:
            self.leftLeftRotation(self.head)

        elif balance_level<-1 and node.val>self.head.right.val:
            self.rightRightRotation(self.head)
        
        elif balance_level>1 and node.val>self.head.left.val:
            self.leftLeftRotation(self.head)
        elif balance_level<-1 and node.val<self.head.right.val:
            self.rigthRightRotate(self.head)


    def leftLeftRotation(self,headNode):
        temp=headNode.left
        t3=temp.right
        temp.right=headNode
        headNode.left=t3
        self.head=temp

        headNode.height = 1 + max(self.depth(headNode.left), 
                        self.depth(headNode.right)) 
        temp.height = 1 + max(self.depth(temp.left), 
                        self.depth(temp.right)) 


    def rigthRightRotate(self,headNode):
        temp=headNode.right
        t3=temp.left
        temp.left=headNode
        headNode.right=t3
        self.head=temp

        headNode.height = 1 + max(self.depth(headNode.left), 
                        self.depth(headNode.right)) 
        temp.height = 1 + max(self.depth(temp.left), 
                        self.depth(temp.right)) 

    def balance(self,headNode):
        if headNode is None:
            return 0
        else:
            return self.depth(headNode.left)-self.depth(headNode.right)




    def depth(self,currentNode):
        if currentNode is None:
            return 0
        total_left=self.depth(currentNode.left)
        total_right=self.depth(currentNode.right)
        return max(total_left,total_right)+1

    def inorder(self, currentNode):
        if currentNode:
            self.inorder(currentNode.left)
            print(currentNode.val, end=' ,')
            self.inorder(currentNode.right)


    def postorder(self, currentNode):
        if currentNode:
            self.postorder(currentNode.left)
            self.postorder(currentNode.right)
            print(currentNode.val, end=' ,')


tree=Tree()
tree.insert(Node(5))
tree.insert(Node(10))
tree.insert(Node(7))
tree.insert(Node(20))
tree.insert(Node(50))
tree.inorder(tree.head)
# tree.postorder(tree.head)
