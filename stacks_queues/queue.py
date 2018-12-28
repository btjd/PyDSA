class Queue(object):
    def __init__(self):
        self.queue = []
        self.size = 0
    
    def isEmpty(self):
        return self.queue == []

    def enqueue(self, item):
        self.queue.insert(0, item)
        self.size += 1

    def dequeu(self):
        if not self.isEmpty():
            self.size -= 1
            return self.queue.pop()
        else:
            return "The queue is already empty"

    def queue_size(self):
        return self.size