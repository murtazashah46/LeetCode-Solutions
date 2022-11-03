import heapq
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution:

    def kthSmallest(self, matrix, k):
        
        maxHeap = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if(k > 0):
                    heappush(maxHeap,-matrix[i][j])
                    k-=1
                elif(matrix[i][j] < -maxHeap[0]):
                    heappop(maxHeap)
                    heappush(maxHeap,-matrix[i][j])
        return maxHeap[0]*-1