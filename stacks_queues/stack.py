class Stack(object):
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, item):
        self.stack.append(item)
        self.size += 1

    def pop(self):
        if not self.isempty():
            self.size -= 1
            return self.stack.pop()
        else:
            return "The stack is already empty"
        

    def peek(self):
        return self.stack[-1]

    def stack_size(self):
        return self.size

    def isempty(self):
        return self.stack == []
