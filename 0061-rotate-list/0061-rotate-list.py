# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if(head == None or head.next == None):
            return head
        
        current = head
        size = 0
        while(current != None):
            size += 1
            current = current.next
        if(k > size):
            k = k%size
        while(k > 0):
            previous = None
            current = head
            while(current.next != None):
                previous = current
                current = current.next
            current.next = head
            previous.next = None
            head = current
            k -= 1
        return head