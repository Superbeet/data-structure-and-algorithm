# Implement a function to check if a linked list is a palindrome

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

    def initialize_palindrome(self):
        last_node = None
        node = None

        x = 20

        for i in range(0,x):

            node = SinglyLinkedListNode()

            node.data = i   # assign some values

            if i is 0:

                self.head = node

            else:

                last_node.next = node

            last_node = node

        for m in range(0,x):

            node = SinglyLinkedListNode()

            node.data = x-1-m   # assign some values

            last_node.next = node

            last_node = node

        return self.head

def traverse(head, loop_point = None):

    data_list = ['head']

    select_node = head

    limit = 50
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


class Stack(object):
    def __init__(self):
        super(Stack, self).__init__()
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        return True

    def pop(self):
        return self.stack.pop()

def isPalindrome_2(head):

    if head is None:
        return False

    fast = head
    slow = head

    stack = Stack()

    while fast is not None and fast.next is not None:
        stack.push(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast is not None:
        slow = slow.next

    while slow is not None:
        if slow.data is not stack.pop():
            return False

        slow = slow.next

    return True

if __name__ == '__main__':
    ll = UnorderedLinkedList()
    head = ll.initialize_palindrome()
    traverse(head)

    # Solution 1
    # reverse the linked list then compare the first half

    # Solution 2
    # Iterative Approach
    is_palindrome = isPalindrome_2(head)
    if is_palindrome:
        print "It is palindrome."
    else:
        print "It is not palindrome."

