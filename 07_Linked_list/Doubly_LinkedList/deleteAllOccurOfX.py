"""
Given the head of a doubly Linked List and a key x . Delete all occurrences of the given key x if it is present and return the new DLL.

Input: 2<->2<->10<->8<->4<->2<->5<->2, x = 2
Output:  10<->8<->4<->5

"""

def deleteAllOccurOfX(head,x):
    if not head:        # if head is None
        return head
    
    current = head
    while current:
        if current.val == x:
            if current.prev:   # if current.prev is not None
                current.prev.next = current.next
            else:
                head = current.next         # delete head node
            
            if current.next:        # if current.next is not None
                current.next.prev = current.prev
                
        current = current.next      # move current pointer forward
        
    return head