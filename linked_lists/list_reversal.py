class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None

def reverse(head):
    queue = []
    while head is not None:
        current = head
        head = current.nextnode
        current.nextnode = None
        queue.append(current)
    while queue:
        current = queue.pop(0)
        if head == None:
            head = current
        else:
            current.nextnode = head
            head = current

def reverse_in_place(head):
    curr_node = head
    prev_node = None
    next_node = None

    while curr_node:
        next_node = curr_node.nextnode
        curr_node.nextnode = prev_node
        prev_node = curr_node
        curr_node = next_node
    return prev_node

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

print a.nextnode.value
print b.nextnode.value
print c.nextnode.value
# print d.nextnode.value

# reverse(a)
reverse_in_place(a)

print d.nextnode.value
print c.nextnode.value
print b.nextnode.value
# print a.nextnode.value