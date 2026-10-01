class Node:
    def __init__(self,val):
        self.val = val          # data stored in the node
        self.next = None        # pointer to the next node
        self.prev = None        # pointer to previous node
    
class Doubly_LinkedList:
    def __init__(self):
        self.head = None
        
    
    # Insert at head
    def insert_at_head(self,val):
        new_node = Node(val)
        
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head       # new_node --> self.head
            self.head.prev = new_node       # new_node <-- self.head
            self.head = new_node            # self.head = new_node
    
    
    
    # Insert at end
    def insert_at_end(self,val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:     # while current.next is not None:
                current = current.next  # find last node
            current.next = new_node # connect current.next to new_node
            new_node.prev = current # connect new_node.prev to current
    
    
    
    # Insert at Specific position
    def insert_at(self,val,position):
        new_node = Node(val)
        if position == 0:
            new_node.next  = self.head

            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return 
        
        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1
        if current is None:
            return("Position is out of bounds")
        new_node.next = current.next    # connect new_node to next node
        new_node.prev = current         # point new_node.prev to current
        
        if current.next:        # current.next is not None:
            current.next.prev = new_node    # updates next node's prev pointer
        current.next = new_node         # connect current node to new_node
        
        
    # Traverse the linked list
    def show_forward(self):
        current = self.head
        while current:
            print(current.val, end="-->")
            current = current.next
        print("None")
        
    def show_backword(self):
        current = self.head
        while current.next:
            current = current.next
            
        while current:
            print(current.val,end="-->")
            current = current.prev
        print("None")
        
        
# TEST
dll = Doubly_LinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)
dll.insert_at_end(40)
dll.insert_at_end(50)
dll.insert_at_end(60)
dll.insert_at_end(70)
dll.show_forward()
dll.show_backword()

        
        
        
            
            