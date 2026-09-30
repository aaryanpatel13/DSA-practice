"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).


"""
# Importing methods to create and show linked from linked list template for local testing
from linkedList_template import createLinkedList, showList


#                               Brute Force Approach
# Use set to store the nodes and keep on checking if any node is already in the set.

# def hasCycle(head):
#     current = head
#     traced = set()      # store the visited node
#     while current:      # while current is not None:
#         if current in traced:       # if the node is already checked brefore
#             return False            # Cycle found
#         traced.add(current)         # add node in the set
#         current = current.next      # move current pointer forward
#     return False                # no repeated node found



#                       Optimal Solutions
#                   Floyd’s Cycle Detection – Two Pointers

"""
1.Set Up Two Runners: Create two pointers: slow (moves 1 step) and fast (moves 2 steps)
2.Start the Race: Both start from the head of the linked list
3.Move at Different Speeds: Slow moves 1 node at a time, fast moves 2 nodes at a time
4.Check for Meeting: If there's a cycle, fast will eventually catch up to slow
5.Check for End: If fast reaches the end (None), there's no cycle

"""

def hasCycle(head):
    slow = head     # slow pointer(tortoise)
    fast = head     # fast pointer(hare)
    while fast and fast.next:   # while fast is not None and fast.next is not None:
        slow = slow.next        # move slow pointer 1 step
        fast = fast.next.next   # move fast pointer 2 step
        if slow == fast:        # check if slow and fast pointer are on the same node
            return True         # cycle found
    return False                # fast pointer reached to end; no cycle found