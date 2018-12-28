class Queue2Stacks(object):
    
    def __init__(self):
        
        # Two Stacks
        self.stack1 = []
        self.stack2 = []
     
    def enqueue(self,element):
        '''
        stack1 is for enqueing and stack2 is for dequeing
        -For enqueing we always just push to stack1
        -For dequeing, if there are any elements in stack2,
         we keep popping and until it's empty, meanwhile any
         subsequent enqueues are always sent to stack1. Once 
         stack2 is empty, we can fill it up again with contents
         from stack1 by poping from stack1 and pushing to stack2
         in order to reverse the order.
        '''
        
        self.stack1.append(element)
    
    # def dequeue(self):
    #     lenght1 = len(self.stack1)
    #     if lenght1 > 1:
    #         for i in range(1, lenght1):
    #             self.stack2.append(self.stack1.pop())
    #         ret = self.stack1.pop()
    #         length2 = len(self.stack2)
    #         for i in range(length2):
    #             self.stack1.append(self.stack2.pop())
    #     elif lenght1 == 1:
    #         ret = self.stack1.pop()
    #     else:
    #         ret = "Nothing to dequeu"
    #     return ret

    def dequeue(self):
        # If stack2 is not empty
        if not self.stack2:
            # while there are elements in stack1
            while self.stack1:
                # reverse order of elements by 
                # transfering them from one stack
                # to the other.
                self.stack2.append(self.stack1.pop())
        # We pop either if stack2 is not empty, or it
        # is empty but we transfered elements from 
        # stakc1 to stack2 first.
        return self.stack2.pop()


if __name__ == "__main__":
    q = Queue2Stacks()
    for i in xrange(5):
        q.enqueue(i)
    
    # print q.stack1, q.stack2


    for i in xrange(5):
        # print q.stack1, q.stack2
        print q.dequeue()