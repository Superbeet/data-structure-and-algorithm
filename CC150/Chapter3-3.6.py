import sys

class Stack(object):
    def __init__(self, limit=None, value=None):
    	if value:
    		self.queue = value
    	else:
        	self.queue = []

        if limit:
        	self.limit = limit
        else:
        	self.limit = 99

    def push(self, item):
        if len(self.queue) >= self.limit:
            return False
        else:
            self.queue.append(item)
            return True

    def pop(self):
        if len(self.queue) is 0:
            return False
        else:
            return self.queue.pop()

    def peek(self):
    	if len(self.queue) is 0:
    		return False
    	else:
    		return self.queue[-1]

    def length(self):
        return len(self.queue)

    def isEmpty(self):
    	if len(self.queue) is 0:
    		return True
    	else:
    		return False

    def __repr__(self):
        return "stack()"

    def __str__(self):
        return "user defined stack object head->%s" %(self.queue)


def ascend_order(src_stack):

	tmp = None

	target_stack = Stack()

	while not src_stack.isEmpty():

		tmp = src_stack.pop()

		while not target_stack.isEmpty() and target_stack.peek() > tmp:

			src_stack.push(target_stack.pop())

		target_stack.push(tmp)

	return target_stack

if __name__ == '__main__':

	value = [7, 10, 12, 8, 5]

	my_stack = Stack(value=value)

	print my_stack

	print ascend_order(my_stack)





