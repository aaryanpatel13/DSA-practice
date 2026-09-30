"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
Do not modify the linked list.

"""
#                                   Brute Force Approach

def detectCycle(head):
    current = head
    traced = {}      # store the visited node
    while current:      # while current is not None:
        if current in traced:       # if the node is already checked brefore
            return current            # Cycle found; return the node where cycle begins
        traced.add(current)         # add node in the set
        current = current.next      # move current pointer forward
    return False                # no repeated node found






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
        # Find cycle
        slow = slow.next      
        fast = fast.next.next  
        if slow == fast:       # cycle found
            # set slow = head to find the start of cycle
            slow = head 
            while slow != head:
                slow = slow.next
                fast = fast.next
            return slow   
    return None                