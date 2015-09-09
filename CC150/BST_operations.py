# Chapter 4 - 4.1

# Implement a function to check if a binary tree is balanced.

class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def isEmpty(self):
        if self.queue:
            return False
        else:
            return True

class TreeNode(object):
    def __init__(self, data = None):
        self.left = None
        self.right = None
        self.parent = None
        self.data = data

    def getData(self):
        return self.data

    def setData(self, new_data):
        self.data = new_data

class RandomTree(object):
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            current = self.root
            while True:
                if value < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = TreeNode(value)

                elif value > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = TreeNode(value)

                else:
                    break
                    print "value is aleady existing in the tree"

    def bft(self):
        if self.root is None:
            return False

        result = []

        queue = Queue()

        queue.enqueue(self.root)

        while not queue.isEmpty():

            current_node = queue.dequeue()

            result.append(str(current_node.data))

            if current_node.left:

                queue.enqueue(current_node.left)

            if current_node.right:

                queue.enqueue(current_node.right)

        result_string =  "->".join(result)

        print result_string


    def inorder_traverse(self):

        self.result = []

        self.inorder(self.root)

        print "->".join(self.result)

    def inorder(self, node):

        if node is None:

            return False

        self.inorder(node.left)

        self.result.append(str(node.data))

        self.inorder(node.right)

    def preorder_traverse(self):

        self.result = []

        self.preorder(self.root)

        print "->".join(self.result)

    def preorder(self, node):

        if node is None:

            return False

        self.result.append(str(node.data))

        self.preorder(node.left)

        self.preorder(node.right)

    def postorder_traverse(self):

        self.result = []

        self.postorder(self.root)

        print "->".join(self.result)

    def postorder(self, node):

        if node is None:

            return False

        self.postorder(node.left)

        self.postorder(node.right)

        self.result.append(str(node.data))

def getHeight(tree_root):
    if tree_root is None:
        return False

    return max(getHeight(tree_root.left), getHeight(tree_root.right)) + 1

def isBalanced(tree_root):
    if root is None:
        return True

    height_diff = abs(getHeight(tree_root.left) - getHeight(tree_root.right))

    if height_diff > 1:
        return False
    else:
        return isBalanced(tree_root.left) and isBalanced(tree_node.right)

if __name__ == '__main__':
    tree = RandomTree()
    node_list = [12 ,5 ,18, 2, 9,15,19, 13, 17, 16]
    for i in node_list:
        tree.add(i)

    print "tree height -> %s" %getHeight(tree.root)

    print "DFS_traverse ->"
    tree.bft()

    print "inorder_traverse ->"
    tree.inorder_traverse()

    print "preorder_traverse ->"
    tree.preorder_traverse()

    print "postorder_traverse ->"
    tree.postorder_traverse()
