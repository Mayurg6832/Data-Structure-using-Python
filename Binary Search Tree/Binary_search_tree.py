#BST implementation
"""
Functions:
insert
depth
search by key
print level order
print inorder
print preorder
print postorder
"""




class Node:
    def __init__(self,val):
            self.data=val
            self.left=None
            self.right=None

class Tree:
    def __init__(self):
        self.head=None

    def insert(self,node):
        if self.head==None:
            self.head=node
        else:
            currentNode=self.head
            while True:
                if currentNode.data<node.data:
                    if currentNode.right is None:
                        currentNode.right=node
                        break
                    currentNode=currentNode.right
                else:
                    if currentNode.left is None:
                        currentNode.left=node
                        break
                    currentNode=currentNode.left
    def depth(self,currentNode):
        if currentNode is None:
            return 0
        total_left=self.depth(currentNode.left)
        total_right=self.depth(currentNode.right)
        return max(total_left,total_right)+1
    def search(self,currentNode,key):
        if currentNode is None:
            print("key {} not found".format(key))
            return False
        elif currentNode.data==key:
            print("key {} if found".format(key))
            return True
        elif currentNode.data>key:
            self.search(currentNode.left,key)
        else:
            self.search(currentNode.right,key)
    
    def lever_order(self,currentNode):
        new_lst=[]
        nodes=[]
        if not currentNode:
            return 
        else:
            for node in currentNode:
                nodes.append(node.data)
                if node.left is not None:
                    new_lst.append(node.left)
                if node.right is not None:
                    new_lst.append(node.right)
            print('<==>'.join([str(x) for x in nodes]))
        self.lever_order(new_lst)



    def inorder(self, currentNode):
        if currentNode:
            self.inorder(currentNode.left)
            print(currentNode.data, end=' ,')
            self.inorder(currentNode.right)


    def preorder(self, currentNode):
        if currentNode: 
            print(currentNode.data, end=' ,')
            self.preorder(currentNode.left)
            self.preorder(currentNode.right)


    def postorder(self, currentNode):
        if currentNode:
            self.postorder(currentNode.left)
            self.postorder(currentNode.right)
            print(currentNode.data, end=' ,')
                



tree=Tree()
# tree.insert(Node(10))
# tree.insert(Node(20))
# tree.insert(Node(5))
# tree.insert(Node(15))
# tree.insert(Node(30))
# tree.insert(Node(2))
# tree.insert(Node(7))
# tree.insert(Node(50))
tree.insert(Node(10))
tree.insert(Node(5))
tree.insert(Node(3))
tree.inorder(tree.head)
print()
tree.preorder(tree.head)
print()
tree.postorder(tree.head)
print()
print(tree.depth(tree.head))
tree.search(tree.head,16)
tree.lever_order([tree.head])