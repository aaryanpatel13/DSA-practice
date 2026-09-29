#                   SINGLY LINKED LIST
"""
A singly linked list is a linear data structure where each element, called a node, contains:
val — the value stored in the node.
next — a pointer/reference to the next node.

"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
class singlyLinkedList:
    def __init__(self):
        self.head = None
        
            
            
                # Insert at the start
    
    def append(self,val):           # appned --> means insert at end
        new_node = Node(val)        # new node created with given value
        if not self.head:   # if self.head is None
            self.head = new_node
        else:
            current = self.head
            while current.next:    # while current.next is not None
                current = current.next
            current.next = new_node
    
    
    
    
    # Display the linked list 
    def traverse(self):            # traverse --> means display the value
        if not self.head:   # if self.head is None
            print("Linked list is empty")
        else:
            current = self.head
            while current:          # while current is not None
                print(current.val, end = "-->") # this will add arrow like this 10 --> 20-->None
                current = current.next
                    
            print("None")
            
            
            
    # Insert at specific location    
    def insertAt(self,val,position):
        new_node = Node(val)
        if position == 0:           # insert at the start
            new_node.next = self.head       
            self.head = new_node
        else:       #  add at any specific position
            current = self.head     # store current head
            prev_node = None        # keep previous head 
            count = 0               # track position
            while current and count < position: # while current is not None and count < position
                prev_node = current
                current = current.next
                count +=1
            prev_node.next = new_node
            new_node.next = current
            
            
          
          
    # Delete Head  
    def deleteHead(self):           # delete head --> delete the first node
        if not self.head:       # if self.head is None --> means linked list is empty
            print("Linked list is empty")   # there's nothing to delete
        else:                           #  store the address of next node in self.head
            self.head = self.head.next  # this will delete the current node
            
            
            
    # Delete from specific postion       
    def delete(self,val):           #delete by value
        if not self.head:
            print(f"{val} is not available.Linked list is empty")
            return
        
        current = self.head     
        if current.val == val:
            self.head = self.head.next
            return
        else:
            prev_node = None
            while current:
                if current.val == val:
                    prev_node.next = current.next
                    return
                prev_node = current
                current = current.next
                
            print(f"{val} not found")
            

        
            
            
            
                  
sll = singlyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
sll.append(60)
sll.traverse()
sll.delete(70)

        
        
