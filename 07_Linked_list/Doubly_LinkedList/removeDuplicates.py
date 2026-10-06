"""
Given a doubly linked list of n nodes sorted by values, remove duplicate nodes present in the linked list.

Input: head: 1<->1<->1<->2<->3<->4
Output: 1<->2<->3<->4
Explanation: Only the first occurance of node with value 1 is retained along with other distinct values. 
"""

def removeDuplicates(head):
    current = head
    look  = current.next
    
    while look:     # while look is not None
        #while look is not None  and current.val == look.val
        while look and current.val == look.val:
            look = look.next
            
        current.next = look # update pointer when unique element found
        
        if look:            # if look is not None
            look.prev = current
            current = look
            look = look.next
    return head
