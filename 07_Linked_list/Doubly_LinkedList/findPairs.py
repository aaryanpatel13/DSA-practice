"""
Given a sorted doubly linked list containing distinct positive integers and an integer target, find all pairs of nodes whose values add up to target.

Input: 1<-->2<-->4<-->5<-->6<-->8<-->9...........this is a doubly linked list
target = 7
Output: [[1, 6], [2, 5]]
Explanation: There are two pairs (1, 6) and (2,5) with sum 7.
"""

#                               Brute Force Approach
#                               Time Complexity: O(N²)
#.                              Space Complexity: O(N)

def findPairs(head,target):
    ans = []            # store answer
    current = head
    while current:      # while current is not None
        nxt = current.next      # next value
        while nxt:      #while nxt is not None
            if nxt.data + current.val == target: 
                ans.append([current.val, nxt.data])
            nxt = nxt.next
        current = current.next
    return ans




#                           Better Approach
#                           Time Complexity: O(N)
#                           Space Complexity: O(N)

def findPairs(head,target):
    current = head
    check = set()           # to keep the track of visited element
    ans = []            # to store ans
    
    while current:          # while current is not None:
        rem = target - current.val          # remaing value 
        if rem in check:            
            ans.append([rem,current.val])
        
        check.add(current.val)
        current = current.next
    return sorted(ans)              # sorted(ans) --> will return the answer in sorted order





#                               Optimal Approach [ Two pointers approach ]
#                               Time Complexity: O(N)
#                               Space Complexity: O(1)

def findPairs(head,target):
    ans = []
    right = head
    while right:                    # while head is not None:
        right = right.next          # send right pointer to the last
        
    left = head
    # left != right --->check left and right same address toh nhi
    # right.next != left --> checks left pointer right ko cross toh nhi kiya 
    while left != right and right.next != left: 
        total = left.val + right.val
        
        if total == target:
            ans.append([left.val,right.val])
            left = left.next
            right = right.prev
        elif total > target:
            right = right.prev
        else:
            left = left.next
    return ans