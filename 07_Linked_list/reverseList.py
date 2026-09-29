# #                   206. Reverse Linked List
# """
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# """

# # Importing methods to create and show linked from linked list template for local testing
from linkedList_template import createLinkedList, showList


# #                           Brute Force Approach
# def reverseList(head):
#     current = head
#     values = []         # to store the value for each node
    
#     while current:          # while current is not None
#         values.append(current.val)
#         current = current.next
    
#     # pop value from values and update each node
#     current = head
#     while current:
#         current.val = values.pop()
#         current = current.next
#     return head

# # Test
# data = [10,20,30,40]
# head = createLinkedList(data)
# showList(head)

# new_head = reverseList(head)
# showList(new_head)


#                   Optimal Approach
# We will reverse the linking of each node


def reverseList(head):
    current = head
    prev_node = None
    
    while current: # while current is not None:
        next_node = current.next # store thet next node before we loose it
        current.next = prev_node # reverse the link of next node : points toward the previous node
        prev_node = current     # move perv_node forward 
        current = next_node     # move current forward
    return prev_node

# Test
data = [10,20,30,40]
head = createLinkedList(data)
showList(head)

new_head = reverseList(head)
showList(new_head)
