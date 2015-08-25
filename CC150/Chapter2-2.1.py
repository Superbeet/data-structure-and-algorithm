#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      507061
#
# Created:     24/08/2015
# Copyright:   (c) 507061 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sys
import os

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

        data_list = ['head']

##        i = 0

        while(select_node):
##            print "round %d - %s" %(i, select_node.data)
##            i = i + 1
            print select_node.data

            data_list.append(str(select_node.data))

            select_node = select_node.next

        print "->".join(data_list)

def remove_duplicate(head_node):

    if head_node is None:
        print "Linked List is NULL"
        return False

    hash_list = []

    select_node = head_node

    while(select_node):

        if select_node.next.data not in hash_list:
            hash_list.append(select_node.data)

        else:
            select_node.next = select_node.next.next

        select_node = select_node.next

if __name__ == '__main__':
    main()
