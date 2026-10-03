def reverseDLL(self, head):
    # empty list or single node
    if not head or not head.next:
        return head

    current = head      # Pointer to traverse through the list
    new_head = None     # Will store the new head after reversal

    # Traverse each node and swap prev and next pointers
    while current:
        # Store current.prev temporarily before swapping
        temp = current.prev
        
        # Swap the pointers: prev becomes next, next becomes prev
        current.prev = current.next
        current.next = temp

        # Update new_head to current node (last processed becomes new head)
        new_head = current

        # Move to the "next" node (which is actually current.prev after swap)
        current = current.prev

    return new_head
