#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      507061
#
# Created:     13/08/2015
# Copyright:   (c) 507061 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os

class DoublyLinkedListNode(object):
    def __init__(self):
        self.next = None
        self.data = None
        self.previous = None

    def getData(self):
        return self.data

    def setData(self, new_data):
        self.data = new_data

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
        self.head = SinglyLinkedListNode()
        self.tail = SinglyLinkedListNode()

    def initialize(self):
        last_node = None
        node = None

        for i in range(0,10):
            node = SinglyLinkedListNode()

            node.data = str(i + 1)   # assign some values

            if i is 0:

                self.head = node

            else:

                last_node.next = node

            last_node = node

        return self.head

    def traverse(self):

        select_node = self.head

        data_list = []

##        i = 0

        while(select_node):
##            print "round %d - %s" %(i, select_node.data)
##            i = i + 1
            print select_node.data

            data_list.append(str(select_node.data))

            select_node = select_node.next

        print "->".join(data_list)

    def insert(self, index, data):

        select_node = self.head

        i = 0

        while(select_node and i is not index-1):

            select_node = select_node.next

            i = i + 1

        new_node = SinglyLinkedListNode()

        new_node.data = data

        new_node.next = select_node.next

        select_node.next = new_node

        new_node.next

        return

    def reverseByLoop(self, head = None):
        """ Reverse the linked list
            Non-recursive method
            - Move the following nodes to the head
        """
        if not head:
            head = self.head

        if not head.next:

            return head

        p = head

        q = head.next

        head.next = None   ## very important

        while(q):
            r = q.next
            q.next = p
            p = q
            q = r

        head = p

        return head

if __name__ == '__main__':

    ll = UnorderedLinkedList()

    ll.initialize()

    ll.traverse()

    ll.insert(6, "new")

    ll.traverse()

    ll.reverseByLoop()

    ll.traverse()