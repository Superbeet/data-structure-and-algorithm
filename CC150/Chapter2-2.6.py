#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      507061
#
# Created:     28/08/2015
# Copyright:   (c) 507061 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from random import randint

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

    def initialize_ll(self):
        last_node = None
        node = None

        x = 20

        for i in range(0,x):
            node = SinglyLinkedListNode()

            n = randint(0,x)
            node.data = n   # assign some values

            if i is 0:

                self.head = node

            else:

                last_node.next = node

            last_node = node

        return self.head

    def initialize_loop_ll(self):
        last_node = None
        node = None

        x = 20

        for i in range(0,x):
            node = SinglyLinkedListNode()

            n = randint(0,x)
            node.data = n   # assign some values

            if i is 0:

                self.head = node

            else:

                last_node.next = node

            last_node = node

        m = randint(0,x)

        select_node = self.head

        for j in range(0,m):

            select_node = select_node.next

        print "loop point No.%d - Data:%s" %(m+1, select_node.data)

        last_node.next = select_node

        return self.head, m+1

def traverse(head, loop_point = None):

    data_list = ['head']

    select_node = head

    limit = 30
    i = 0

    while(select_node and i < limit):
        i = i + 1
    ##            print "round %d - %s" %(i, select_node.data)
        if i == loop_point:
            data_list.append("[%s]"%str(select_node.data))
        else:
            data_list.append(str(select_node.data))

        select_node = select_node.next

    print "=>".join(data_list)

def check_loop(head):

    if head is None or head.next is None:
        return False

    fast_runner = head
    slow_runner = head

    while fast_runner is not None and fast_runner.next is not None:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        if fast_runner is slow_runner:
            break

    if fast_runner is slow_runner:
        return fast_runner

    else:
        return False

def find_loop_beginning(head):

    if head is None or head.next is None:
        return False

    collision_node = check_loop(head)

    if collision_node:
        front_runner = head
        rear_runner = collision_node

        while front_runner is not rear_runner:

            front_runner = front_runner.next
            rear_runner = rear_runner.next

        return front_runner

    else:
        return False


if __name__ == '__main__':
    ll = UnorderedLinkedList()

    head, loop_point = ll.initialize_loop_ll()
    traverse(head, loop_point)

    # head = ll.initialize_ll()
    # traverse(head)

    # loop_exsit = check_loop(head)
    # if loop_exsit:
    #     print "loop is existing"
    # else:
    #     print "loop is not existing"

    loop_beginning = find_loop_beginning(head)
    if loop_beginning:
        print "loop beginning point -> %s" %(loop_beginning.data)


