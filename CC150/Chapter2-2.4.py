#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      507061
#
# Created:     26/08/2015
# Copyright:   (c) 507061 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

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

            node.data = int(i % 10 + 1)   # assign some values

            if i is 0:

                self.head = node

            else:

                last_node.next = node

            last_node = node

        return self.head

def traverse(head):

    data_list = ['head']

    select_node = head
    ##        i = 0

    while(select_node):
    ##            print "round %d - %s" %(i, select_node.data)
    ##            i = i + 1
        # print select_node.data

        data_list.append(str(select_node.data))

        select_node = select_node.next

    print "->".join(data_list)


def partition_linkedlist_1(head, pivot):
    """ Append to the end
    """
    beforeStart = None
    beforeEnd = None
    afterStart = None
    afterEnd = None

    node = head

    while(node is not None):
        next = node.next
        node.next = None

        if node.data < pivot:
            if not beforeStart:
                beforeStart = node
                beforeEnd = beforeStart
            else:
                beforeEnd.next = node
                beforeEnd = node

        else:
            if not afterStart:
                afterStart = node
                afterEnd = afterStart
            else:
                afterEnd.next = node
                afterEnd = node

        node = next

    if beforeStart is None:
        return afterStart

    beforeEnd.next = afterStart

    return beforeStart

def partition_linkedlist_2(head, pivot):
    """ Insert to the start
    """
    beforeStart = None
    beforeEnd = None
    afterStart = None
    afterEnd = None

    node = head

    while(node is not None):
        next = node.next
        node.next = None

        if node.data < 5:
            if not beforeStart:
                beforeStart = node
                beforeEnd = beforeStart
            else:
                node.next = beforeStart
                beforeStart = node
        else:
            if not afterStart:
                afterStart = node
                afterEnd = afterStart
            else:
                node.next = afterStart
                afterStart = node

        node = next

    if not beforeStart:
        return afterStart

    beforeEnd.next = afterStart

    return beforeStart


if __name__ == '__main__':
    ll = UnorderedLinkedList()
    head = ll.initialize()
    traverse(head)

    new_head = partition_linkedlist_2(head, 5)
    traverse(new_head)
