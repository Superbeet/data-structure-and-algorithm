# Chapter 4 - 4.3

# Given a sorted(increasing order) array with unique integer 
# elements, write an algorithm to create a binary search tree
# with minimal height

from structure import Queue

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

def bft(root_node):
    if root_node is None:
        return False

    result = []

    queue = Queue()

    queue.enqueue(root_node)

    while not queue.isEmpty():

        current_node = queue.dequeue()

        result.append(str(current_node.data))

        if current_node.left:

            queue.enqueue(current_node.left)

        if current_node.right:

            queue.enqueue(current_node.right)

    result_string =  "->".join(result)

    print result_string


def print_out_tree(root_node):
    if root_node is None:
        return False

    result = []

    level = 0

    last_level = -1

    level_queue = Queue()

    queue = Queue()

    queue.enqueue(root_node)

    level_queue.enqueue(level)

    while not queue.isEmpty():

        current_node = queue.dequeue()

        current_level = level_queue.dequeue()

        # result.append(str(current_node.data))

        result.append(str(current_node.data))

        # print "%s" %(current_node.data)

        level += 1

        if current_node.left:

            queue.enqueue(current_node.left)

            level_queue.enqueue(level)

        if current_node.right:

            queue.enqueue(current_node.right)

            level_queue.enqueue(level)

        print "  ".join(result)


        if current_level is not last_level:

        	result = []

        	last_level = current_level

    # result_string =  "->".join(result)

    # print result_string

def createMinimalBST(array, start, end):
	if start > end:
		return None

	mid = (start + end)/2
	tree_node = TreeNode(array[mid])

	tree_node.left = createMinimalBST(array, start, mid-1)
	tree_node.right = createMinimalBST(array, mid+1, end)

	return tree_node

def startCreateMinimalBST(list):
	return createMinimalBST(list, 0, len(list)-1)

if __name__ == '__main__':

    node_list = [1 ,3 ,4, 5, 8, 10, 11, 12, 13, 15]

    root_node = startCreateMinimalBST(node_list)

    bft(root_node)

    print_out_tree(root_node)
