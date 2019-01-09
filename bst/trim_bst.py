class Node(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def trim_bst(root, minim, maxim):
    if not root:
            return
    root.left = trim_bst(root.left, minim, maxim)
    root.right = trim_bst(root.right, minim, maxim)
    if minim <= root.val <= maxim:
        return root
    if root.val < minim:
        return root.right
    if root.val > maxim:
        return root.left

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

class TestTrimBst(object):

    def test_trim_bst(self, sol):
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

        assert sol(eight, 5, 13) == eight

        print 'ALL TEST CASES PASSED'

# Run Tests
t = TestTrimBst()
t.test_trim_bst(trim_bst)

# eight = Node(8)
# three = Node(3)
# ten = Node(10)
# one = Node(1)
# six = Node(6)
# fourteen = Node(14)
# four = Node(4)
# seven = Node(7)
# thirteen = Node(13)

# eight.left = three
# eight.right = ten
# three.left = one
# three.right = six
# ten.right = fourteen
# six.left = four
# six.right = seven
# fourteen.left = thirteen
# ret = trim_bst(eight, 5, 13)
# print(ret.val, type(ret))