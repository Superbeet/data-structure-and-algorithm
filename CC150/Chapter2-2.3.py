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

#---------------------------------------------------------------------------
# Implementation starts from here
#---------------------------------------------------------------------------
def delete_node(node):
    if not node:
        return False

    # Copy all data from next node
    if node.next:
        node.data = node.next.data
        node.next = node.next.next

    return True


if __name__ == '__main__':
    ll = UnorderedLinkedList()
    head = ll.initialize()
    ll.traverse()

    n = 0
    while n < 10:
        head = head.next
        n += 1

    print "delete %dth node - %s" %(n, head.data)
    delete_node(head)

    ll.traverse()

