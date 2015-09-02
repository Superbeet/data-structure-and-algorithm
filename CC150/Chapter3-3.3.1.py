import sys
import os

class MyStack(object):
    def __init__(self, limit):
		super(MyStack, self).__init__()
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

    def peek(self):
        if not len(self.queue):
        	return False

        return self.queue[-1]

class SetOfStack(object):
    def __init__(self):
		self.stack_volumn = 10
		self.last_stack = 0
		self.stack_pool = []
		new_stack = MyStack(self.stack_volumn)
		self.stack_pool.append(new_stack)

    def pop(self):
        if self.stack_pool[self.last_stack].length() == 0:
            self.stack_pool.pop()
            self.last_stack -= 1
            return self.stack_pool[self.last_stack].pop()

        return self.stack_pool[self.last_stack].pop()

    def push(self, item):
		if self.stack_pool[self.last_stack].length() == self.stack_volumn:
			new_stack = MyStack(self.stack_volumn)
			print "create a new stack"
			self.stack_pool.append(new_stack)
			self.last_stack += 1

		self.stack_pool[self.last_stack].push(item)

		return True

    def peek(self):
        return self.stack_pool[self.last_stack].peek()

    def popAt(self, index):
        return self.stack_pool[index].pop()

if __name__ == '__main__':
    ss = SetOfStack()

    for i in range(0,100):
    	ss.push(i)

    for n in range(0,12):
       ss.pop()

    print ss.peek()

    for m in range(0,12):
        print ss.popAt(1)

