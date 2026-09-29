# ============================================================
# Reusable Linked List Template for Local Testing
# Use this template to create and traverse linked lists
# in future linked-list problems.
# ===========================================================

class Node:
    def __init__(self,val):
        self.val = val      
        self.next = None
        
    
def createLinkedList(data):
    if not data:
        return None
    head = Node(data[0])
    
    current = head
    for val in data[1:]:
        current.next = Node(val)
        current = current.next
    return head

def showList(head):
    if not head:
        print("Linked list is empty")
        
    current = head
    while current:
        print(current.val,end="-->")
        current = current.next
    print("None")


# Test 
# head = [10,20,30,40]
# ll = createLinkedList(head)
# showList(ll)
