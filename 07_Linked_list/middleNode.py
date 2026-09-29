#                876. Middle of the Linked List
"""
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

"""

# # Importing methods to create and show linked from linked list template for local testing
from linkedList_template import createLinkedList, showList

#                                Brute Force Approach
def middleNode(head):
    lenght = 0
    current = head
    # Traversing to find the total no. of Nodes
    while current:  # while current is not None:
        current = current.next
        lenght += 1
    if lenght % 2 == 0:
        mid = lenght // 2       # mid position of linked list
    # Traversing again to find the Node at middle position
    current = head
    for _ in range(mid):
        current = current.next
    return current

# Test
data = [1,2,3,4,5,6]
head = createLinkedList(data)
showList(head)
ans = middleNode(head)
print(ans.val)
showList(ans)


#                       Optimal Solution 
#                       Tortoise - Hare Method
""" 
In this method we take two pointers: fast and slow
fast will move 2 steps at a point i.e. :
fast += 2
slow will move 1 steps at a point i.e. :
slow += 1

"""
def middleNode(head):
    if not head:
        return None
    fast = head
    slow = head
    while fast and  fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


# Test
data = [1,2,3,4,5,6]
head = createLinkedList(data)
showList(head)
result = middleNode(head)
print(result.val)
showList(result)