#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      507061
#
# Created:     11/08/2015
# Copyright:   (c) 507061 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Stack(object):
    def __init__(self, limit):
        self.queue = []
        self.limit = limit

    def push(self, item):
        if len(self.queue) is self.limit:
            return False
        else:
            self.queue.append(item)
            return True

    def pop(self):
        if len(self.queue) is 0:
            return False
        else:
            return self.queue.pop()

    def length(self):
        return len(self.queue)

    def __repr__(self):
        return "stack()"

    def __str__(self):
        return "user defined stack object %s" %(self.queue)

class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def isEmpty(self):
        if self.queue:
            return False
        else:
            return True

class SpecialQueue(object):
    def __init__(self, limit):
        self.S1 = Stack(limit)
        self.S2 = Stack(limit)
        self.limit = limit

    def enqueue(self, item):
        if self.S1.length() is self.limit:
            print "Stop to push item in, SpecialQueue will overflow"
            return False
        else:
            self.S1.push(item)
            return True

    def dequeue(self):
        if self.S2.length() is 0:
            # copy all items from stack S1 to S2
            while(self.S1.length() is not 0):
                self.S2.push(self.S1.pop())

        if self.S2.length() is 0:
            print "Stop to pop item out, SpecialQueue will underflow"
            return False

        else:
            return self.S2.pop()

    def __repr__(self):
        return "Special Queue Class"

    def __str__(self):
        return "S1 -> %s\nS2 -> %s\n" %(self.S1, self.S2)

def main():
##    S = stack(5)
##    S.push(9)
##    S.push(2)
##    S.push(3)
##    S.push(5)
##    print S
##
##    print S.pop()
##    print S
##    print S.pop()
##    print S

    SS = SpecialQueue(8)
    SS.enqueue(1)
    SS.enqueue(2)
    SS.enqueue(3)
    SS.enqueue(4)
    SS.enqueue(5)
    SS.enqueue(6)
    SS.enqueue(7)
    SS.enqueue(8)
    SS.enqueue(9)

    print SS

    SS.dequeue()
    print SS

    SS.dequeue()
    print SS

    SS.dequeue()
    SS.dequeue()
    SS.dequeue()
    SS.dequeue()
    SS.dequeue()
    SS.dequeue()
    SS.dequeue()

    print SS


if __name__ == '__main__':
    main()
