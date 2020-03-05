class Node:
    def __init__(self,value):
      self.head = None
      self.value = value

class Linklist:

    def __init__(self):
        self.root = None
        self.head = self.root
    
    def addNode(self, value):
        if self.root == None:
            head = Node(value)
            self.root = head
            self.head = head
        else:
            n = Node(value)
            self.root.head = n
            self.root = n

    def printAll(self):
        temp = self.head 
        print("------------")

        while temp != None:
            print(temp.value)
            temp = temp.head

    def addNodeInNthPostion(self,nth,value):
        temp = self.head
        position = 1
        while temp != None:
            if position == nth:
                newNode = Node(value)
                forwardNode = temp.head
                temp.head = newNode
                temp.head.head = forwardNode
            position += 1
            temp = temp.head

    def addNodeInTheBeging(self,val):
        newNode = Node(val)
        newNode.head = self.head
        self.head = newNode
    
    def addNodeInTheLast(self, val):
        temp = self.head 
        while temp.head != None:
            temp = temp.head
        
        newNode = Node(val)
        temp.head = newNode

instruction = """
    Enter your command\n
    1 : Add Node
    2 : Print All node
    3 : Exit
    """
print(instruction)

link = Linklist()

while True:
    command = int(input(" > "))
    if command == 3:
        break
    elif command == 1:
        while True:
            x = int(input())
            if x == 0:
                break
            link.addNode(x)
    elif command == 2:
        link.printAll()
    

