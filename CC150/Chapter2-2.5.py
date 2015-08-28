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

    def initialize(self):
        last_node = None
        node = None

        for i in range(0,10):
            node = SinglyLinkedListNode()

            n = randint(0,9)
            node.data = n   # assign some values

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

    print "==>".join(data_list)

def traverse_reverse(head):

    data_list = ['head']

    select_node = head
    ##        i = 0

    while(select_node):
    ##            print "round %d - %s" %(i, select_node.data)
    ##            i = i + 1
        # print select_node.data

        data_list.append(str(select_node.data))

        select_node = select_node.next

    data_list = data_list[::-1]

    print "<==".join(data_list)

def sum(num_1, num_2):

    node_1 = num_1
    node_2 = num_2

    head = SinglyLinkedListNode()

    carry = 0

    sum_node = head

    while node_1 and node_2 or carry > 0:

        if not node_1:
            node_1_data = 0
        else:
            node_1_data = node_1.data

        if not node_2:
            node_2_data = 0
        else:
            node_2_data = node_2.data

        digit_sum = node_1_data + node_2_data + carry
##        print "node_1.data+node_2.data+carry -> %s+%s+%s" %(node_1.data, node_2.data, carry)

        digit = (digit_sum + 10) % 10
        carry = digit_sum / 10
##        print "digit|carry -> %s|%s" %(digit, carry)

        sum_node.data = digit

        if node_1 or node_2:
            sum_node.next = SinglyLinkedListNode()
            sum_node = sum_node.next

        if node_1:
            node_1 = node_1.next

        if node_2:
            node_2 = node_2.next

    return head

if __name__ == '__main__':
    num_1 = UnorderedLinkedList()
    head_1 = num_1.initialize()
    num_2 = UnorderedLinkedList()
    head_2 = num_2.initialize()
    traverse_reverse(head_1)
    traverse_reverse(head_2)

    sum_value = sum(head_1, head_2)
    traverse_reverse(sum_value)
