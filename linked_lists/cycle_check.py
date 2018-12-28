class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None

def cycle_check(node):
    current = node.nextnode
    found = False
    while not found:
        if current.nextnode == None:
            return False
        elif current.nextnode == node:
            found = True
        else:
            current = current.nextnode
    return found

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z


#############
class TestCycleCheck(object):
    
    def test(self,sol):
        assert sol(a) is True
        assert sol(x) is False
        
        print "ALL TEST CASES PASSED"
        
# Run Tests

t = TestCycleCheck()
t.test(cycle_check)