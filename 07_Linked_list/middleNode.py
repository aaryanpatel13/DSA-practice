#               876. Middle of the Linked List
"""
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

"""
# Importing methods to create and show linked from linked list template for local testing
from linkedList_template import createLinkedList, showList



#                               Brute Force Approach
def middleNode(head):
    lenght = 0
    current = head
    
    while current:  # while current is not None:
        current = current.next
        lenght += 1
    mid = lenght // 2
    current = head
    for _ in range(mid):
        current = current.next
    return current


data = [1,2,3,4,5]
head = createLinkedList(data)
showList(head)
ans = middleNode(head)
print(ans.val)
showList(ans)