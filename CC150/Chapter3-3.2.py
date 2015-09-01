#-------------------------------------------------------------------------------
# How would yieldou design a stack which, in addition to push and pop, also has a
# function min which returns the minimum element? Push, pop and min should all
# operate in O(1) time.
#-------------------------------------------------------------------------------

class Stack(object):
    def __init__(self, limit):
        self.stack = []
        self.limit = limit

    def push(self, item):
        if len(self.stack) >= self.limit:
            return False
        else:
            self.stack.append(item)
            return True

    def pop(self):
        if len(self.stack) is 0:
            return False
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) is 0:
            return False
        else:
            return self.stack[-1]

    def length(self):
        return len(self.stack)

    def __repr__(self):
        return "stack()"

    def __str__(self):
        return "user defined stack object %s" %(self.stack)

    def traverse(self):
        print self.stack

class StackWithMin(object):
    def __init__(self, limit):
        self.limit = limit
        self.min = None
        self.stack = Stack(limit)

    def push(self, value):
        if self.stack.length() >= self.limit:
            return False

        if self.min is None:
            self.min = value
        else:
            self.min = min(value, self.min)

        node_with_min = NoteWithMin(value, self.min)
        self.stack.push(node_with_min)
        return True

    def min(self):
        return self.min

    def pop(self):
        if self.stack.length<=0:
            return False

        item = self.stack.pop()
        self.min = self.stack.peek().min

        return item.value

    def traverse(self):
        print self.stack

class NoteWithMin(object):
    def __init__(self, value, min):
        self.value = value
        self.min = min

if __name__ == '__main__':
    stack = StackWithMin(10)

    stack.push(3)
    stack.push(2)
    stack.push(1)
    stack.push(4)

    stack.pop()
    stack.pop()
    stack.pop()

    print stack.min
