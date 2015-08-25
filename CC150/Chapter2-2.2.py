#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      507061
#
# Created:     25/08/2015
# Copyright:   (c) 507061 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Implement an algorithm to find the kth to last element of a singly linked list

class SinglyLinkedListNode(object):
    def __init__(self):
        self.next = None
        self.data = None

    def getData(self):
        return self.data

    def setData(self, new_data):
        self.data = new_data

class UnorderedLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def initialize(self):
        last_node = None
        node = None

        for i in range(0,30):
            node = SinglyLinkedListNode()

            node.data = str(i % 10 + 1)   # assign some values

            if i is 0:

                self.head = node

            else:

                last_node.next = node

            last_node = node

        return self.head

    def traverse(self):

        select_node = self.head

        data_list = ['head']

##        i = 0

        while(select_node):
##            print "round %d - %s" %(i, select_node.data)
##            i = i + 1
            # print select_node.data

            data_list.append(str(select_node.data))

            select_node = select_node.next

        print "->".join(data_list)

# Fast and slow pointers
def last_kth_node_1(head, k):
    if not head:
        print "     linked list is NULL"
        return head

    runner_1 = head
    runner_2 = head

    n = 0

    while n < k:
        runner_2 = runner_2.next
        n = n + 1

    while runner_2:
        runner_1 = runner_1.next
        runner_2 = runner_2.next

    print "     last number %d node is: %s" %(k,runner_1.data)
    return runner_1

# Recursive method
# Only print the value
def last_kth_node_2(head, k):
    if head is None:
        return 0

    n = last_kth_node_2(head.next, k) + 1

    if n == k:
        print "     last number %d node is: %s" %(k,head.data)

    return n

# Recursive methot
# Return the node
class IntWrapper(object):
    def __init__(self):
        self.value = 0

def last_kth_node_3(head, k, i):
    if head is None:
        return False

    node = last_kth_node_3(head.next, k, i)

    i.value = i.value + 1

    if i.value == k:
        print "     last number %d node is: %s" %(k,head.data)
        return head

    return node

if __name__ == '__main__':
    ll = UnorderedLinkedList()
    head = ll.initialize()
    ll.traverse()

    print "last_kth_node_1"
    last_kth_node_1(head, 11)

    print "last_kth_node_2"
    last_kth_node_2(head, 11)

    print "last_kth_node_3"
    i = IntWrapper()
    last_kth_node_3(head, 11, i)
