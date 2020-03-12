class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def preOrder(root):
    if root:
        preOrder(root.right)
        preOrder(root.left)
        print(root.value)


root = Node(1)

root.left = Node(2)
root.right = Node(5)

root.left.left = Node(3)
root.left.right = Node(4)

root.right.left = Node(6)
root.right.right = Node(7)

preOrder(root)