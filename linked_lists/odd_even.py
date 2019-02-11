"""
LeetCode 328
Given a singly linked list, group all odd nodes together followed 
by the even nodes. Please note here we are talking about the node 
number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) 
space complexity and O(nodes) time complexity.
"""

def odd_even_list(head):
    current = head
    previous = None
    stack = []
    count = 1
    while current:
        if count % 2 != 0:
            if previous is None:
                head = current.next
                current.next = None
                stack.append(current)
                current = head
            else:
                previous.next = current.next
                current.next = None
                stack.append(current)
                current = previous.next
        else:
            previous = current
            current = current.next
        count += 1

    while stack:
        node = stack.pop()
        if head is None:
            head = node
        else:
            node.next = head
            head = node
    return head