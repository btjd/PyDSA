class Dequeue(object):
    def __init__(self):
        self.dequeue = []
        self.size = 0

    def isEmpty(self):
        return self.dequeue == []

    def add_front(self, item):
        self.dequeue.insert(0, item)
        self.size += 1

    def add_back(self, item):
        self.dequeue.append(item)
        self.size += 1

    def remove_front(self, item):
        if not self.isEmpty():
            self.size -= 1
            return self.dequeue.pop(0)
        else:
            return "The dequeue is already empty"

    def remove_back(self, item):
        if not self.isEmpty():
            self.size -= 1
            return self.dequeue.pop()
        else:
            return "The dequeu is already empty"