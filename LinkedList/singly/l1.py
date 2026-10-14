'''class Node:
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
l1.display()'''


'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" ")
            current = current.next
        print("None")
my_list = LinkedList()

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

my_list.head = node1
node1.next = node2
node2.next = node3
node3.next = node4

my_list.display()'''


# create singly linkedlist
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def display(self):
        current = self.head

        while current:
            print(current.data, end=" ")
            current = current.next

        print("None")

my_list = LinkedList()

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

my_list.head = node1
node1.next = node2
node2.next = node3
node3.next = node4

my_list.display()
'''

# insert at the beginning

'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head

        while current:
            print(current.data, end =" ")
            current = current.next


my_list = LinkedList()

my_list.insert_beginning(30)
my_list.insert_beginning(20)
my_list.insert_beginning(10)
my_list.insert_beginning(5)

my_list.display()'''



# insert at the end

'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
    
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node


    def insert_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    
    def display(self):
        current = self.head

        while current:
            print(current.data, end=" ")
            current = current.next
        print("None")


my_list = LinkedList()

my_list.insert_end(10)
my_list.insert_end(20)
my_list.insert_end(30)
my_list.insert_end(40)
my_list.insert_end(50)

my_list.insert_beginning(5)

my_list.display()

'''

# insert at the beginning and end

'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" ")
            current = current.next
        print("None")
    def insert_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head =  new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next
        current.next = new_node
    
mylist = LinkedList()

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)


mylist.head = node1
node1.next = node2
node2.next = node3
node3.next = node4


mylist.display()
mylist.insert_beginning(5)
mylist.display()
mylist.insert_end(45)
mylist.display()'''


# insert at any postion in singly linkedlist

'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def inser_at_position(self, data, position):
        if position < 1:
            print("Invalid position")
            return
        new_node = Node(data)

        if position == 1:
            new_node.next = self.head
            self.head =  new_node
            return new_node

        current = self.head
        count = 1

        while current.next is not None and count < position -1:
            current = current.next
            count += 1

        if current is None:
            print("Invalid position")
            return

        new_node.next = current.next 
        current.next = new_node

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" ")
            current = current.next
        print("None")


mylist = LinkedList()

mylist.inser_at_position(10, 1)
mylist.inser_at_position(20, 2)
mylist.inser_at_position(30, 3)
mylist.inser_at_position(40, 4)
mylist.inser_at_position(50, 2)

mylist.display()'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head

        while current:
            print(current.data, end=" ")
            current = current.next
        print("None")
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.next
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head

        while current.next.next is not None:
            current  =  current.next
        current.next = None

    def delete_at_position(self, position):
        

mylist = LinkedList()

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)


mylist.head = node1
node1.next = node2
node2.next = node3

mylist.display()