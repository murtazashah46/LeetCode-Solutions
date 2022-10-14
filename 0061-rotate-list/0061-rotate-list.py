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
        if(k >= size):
            k = k%size
        if(k == 0):
            return head
        
        first = head
        second = head
        while(k > 0):
            first = first.next
            k -= 1
        while(first.next != None):
            first = first.next
            second = second.next
        first.next = head
        head = second.next
        second.next = None
        return head