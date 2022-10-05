# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        binary = ""
        while(head.next != None):
            binary += str(head.val)
            head = head.next
        binary += str(head.val)
        return int(binary,2)