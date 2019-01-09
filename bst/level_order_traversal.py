class Node(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    if not root:
        return []
    # Initialize our output with the root node
    lot_nodes = [[root]]
    # While the latest level contains nodes that have at
    # least one child (we have not reached lowest level)
    while [n for n in lot_nodes[-1] if (n.left or n.right)]:
        # Create a new level and add to it all children from
        # the previous node.
        new_level = []
        for node in lot_nodes[-1]:
            if node.left:
                new_level.append(node.left)
            if node.right:
                new_level.append(node.right)
        # Add a copy of new level to lot_nodes before
        # we reset it in the next for loop iteration
        lot_nodes.append(new_level[:])
    # List comprehension to convert output from Node
    # to value representation
    lot_vals = [[n.val for n in level] for level in lot_nodes]
    return lot_vals

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

class TestLevelOrder(object):

    def test_level_order(self, sol):
        one = Node(1)
        two = Node(2)
        three = Node(3)
        four = Node(4)
        five = Node(5)
        six = Node(6)
        one.left = two
        one.right = three
        two.left = four
        three.left = five
        three.right = six
        assert sol(one) == [[1], [2, 3], [4, 5, 6]]

        three = Node(3)
        nine = Node(9)
        twenty = Node(20)
        fifteen = Node(15)
        seven = Node(7)
        three.left = nine
        three.right = twenty
        twenty.left = fifteen
        twenty.right = seven
        assert sol(three) == [[3], [9, 20], [15, 7]]

        eight = Node(8)
        three = Node(3)
        ten = Node(10)
        one = Node(1)
        six = Node(6)
        fourteen = Node(14)
        four = Node(4)
        seven = Node(7)
        thirteen = Node(13)
        eight.left = three
        eight.right = ten
        three.left = one
        three.right = six
        ten.right = fourteen
        six.left = four
        six.right = seven
        fourteen.left = thirteen
        assert sol(eight) == [[8], [3, 10], [1, 6, 14], [4, 7, 13]]

        print 'ALL TEST CASES PASSED'

# Run Tests
t = TestLevelOrder()
t.test_level_order(level_order_traversal)