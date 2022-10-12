# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current = head        
        before_left = None
        counter = 1
        if(current.next == None or left == right):
            return head
        
        while(counter < left):
            if(current.next == None):
                return head
            before_left = current
            current = current.next
            counter += 1
        
        was_left = current
        
        previous = None
        while(counter <= right):
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
            counter += 1
        if(before_left != None):
            before_left.next = previous
        else:
            head = previous
        was_left.next = current

        return head