class Node:
    def __init__(self, data):
        self.data = data 
        
class LinkedList:
    def __init__(self):
        self.head = None
    def display(self):
        current = self.head

        while current:
            print(current.data, end=" → ")
            current = current.next

        print("None")

l1 = LinkedList()

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)


l1.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
l1.display()
    