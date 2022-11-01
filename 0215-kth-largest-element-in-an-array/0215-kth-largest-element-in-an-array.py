import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = nums
        for i in range(len(minHeap)):
            minHeap[i] = minHeap[i]*-1
        heapify(minHeap)
        return nsmallest(k,minHeap)[k-1]*-1