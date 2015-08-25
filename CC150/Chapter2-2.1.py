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

def remove_duplicate(head_node):

    if head_node is None:
        print "Linked list is NULL"
        return False

    hash_list = []

    last_node = None

    select_node = head_node

    while(select_node):

        # print hash_list, select_node.data

        if select_node.data not in hash_list:

            hash_list.append(select_node.data)

            last_node = select_node

        else:

            last_node.next = select_node.next

        select_node = select_node.next

    return head_node

def remove_duplicate_no_buffer_2(head_node):
    """ Use two pointers
        one extra pointer
    """

    if head_node is None:
        print "Linked list is NULL"
        return False

    select_node = head_node

    while(select_node):

        compare_node = select_node.next

        while(compare_node):

            last_node = select_node

            if compare_node.data == select_node.data:  
                # print "     remove_node->",compare_node.data
                # print "     compare_node.next->",compare_node.next
                # print "     last_node->", last_node.data
                last_node.next = compare_node.next

            else:

                last_node = compare_node

            compare_node = compare_node.next

        select_node = select_node.next

def remove_duplicate_no_buffer_1(head_node):
    """ Use two pointers
        no extra space
    """

    if head_node is None:
        print "Linked list is NULL"
        return False

    select_node = head_node

    while select_node:

        runner = select_node

        while runner.next:

            if runner.next.data == select_node.data:

                runner.next = runner.next.next

            else:

                runner = runner.next

        select_node = select_node.next

    return head_node

if __name__ == '__main__':

    ll = UnorderedLinkedList()

    head = ll.initialize()

    ll.traverse()

    # remove_duplicate(head)

    # ll.traverse()

    # remove_duplicate_no_buffer_1(head)
    remove_duplicate_no_buffer_2(head)

    ll.traverse()