class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None

def nth_to_last_node(n, head):
    length = 0
    current = counter = head
    while counter:
        counter = counter.nextnode
        length += 1
    p = 0
    while p < length - n:
        current = current.nextnode
        p += 1
    return current.value

def instructor_version(n, head):
    left = head
    right = head

    for i in xrange(n-1):
        if not right.nextnode:
            raise LookupError("n is out of bounds")
        right = right.nextnode
    while right.nextnode:
        left = left.nextnode
        right = right.nextnode
    return left

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)
i = Node(9)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e
e.nextnode = f
f.nextnode = g
g.nextnode = h
h.nextnode = i

target_node = nth_to_last_node(4, a)
print(target_node)