# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        mergedList = []
        for i in range(len(lists)):
            while(lists[i]!= None):
                mergedList.append(lists[i].val)
                lists[i] = lists[i].next
        mergedList = sorted(mergedList)
        head = tail = None
        for i in range(len(mergedList)):
            node = ListNode(mergedList[i])
            if(head == None):
                head = tail = node
            else:
                tail.next = node
                tail = tail.next
        return head
        