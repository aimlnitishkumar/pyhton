'''
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def preorder(root):

    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")
root = TreeNode(10)

root.left = TreeNode(5)
root.right = TreeNode(15)

root.left.left = TreeNode(3)
root.left.right = TreeNode(7)


root.right.left = TreeNode(12)
root.right.right = TreeNode(20)


inorder(root)
print()
preorder(root)
print()
postorder(root)
'''


'''class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def inoder(root):
    if root is None:
        return

    inoder(root.left)
    print(root.data, end=" ")
    inoder(root.right)

def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")

root = TreeNode(10)

root.left = TreeNode(5)
root.right = TreeNode(15)

root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

inoder(root)
print()
preorder(root)
print()
postorder(root)'''



# LEVEL ORDER TRAVERSAL = BFS (Breadth-First Search)


'''from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def level_order(root):
    if root is None:
        return

    queue = deque()

    queue.append(root)

    while queue:
        node = queue.popleft()

        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

root = TreeNode(10)

root.left = TreeNode(5)
root.right = TreeNode(15)

root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

root.right.left = TreeNode(12)
root.right.right = TreeNode(20)

level_order(root)'''


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def search(root, target):
    if root is None:
        return False
    if target == root.data:
        return True
    if target > root.data:
        return search(root.right, target)
    
    return search(root.left, target)

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value > root.data:
        root.right = insert(root.right, value)

    if value < root.data:
        root.left = insert(root.left, value)
    return root


def delete(root, value):
    if root is None:
        return None
    if value < root.data:
        root.left = delete(root.left, value)

    elif value > root.data:
        root.right = delete(root.right, value)

    else:
        # Case 1: No left child
        if root.left is None:
            return root.right

        # Case 2: No right child
        if root.right is None:
            return root.left

        # Case 3: Two children
        successor = root.right

        while successor.left:
            successor = successor.left

        root.data = successor.data

        root.right = delete(root.right, successor.data)

    return root

    
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)

root.left.left = TreeNode(20)
root.left.right = TreeNode(40)


root.right.left = TreeNode(60)
root.right.right = TreeNode(80)


inorder(root)
print()
root = insert(root, 65) 
inorder(root)
print()
root = insert(root, 5)
inorder(root)

print()
root = delete(root, 70)
inorder(root)