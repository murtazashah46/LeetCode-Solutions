# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        arr = [] 
        while(head.next != None):
            arr.append(head.val)
            head = head.next    
        arr.append(head.val)
        if(arr != arr[::-1]):
            return False
        return True