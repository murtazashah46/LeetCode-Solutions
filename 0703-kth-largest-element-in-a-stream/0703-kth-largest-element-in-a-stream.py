import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        self.k = k
        for i in range(len(nums)):
            if(self.k>0):
                heappush(self.minHeap,nums[i])
                self.k -= 1
            elif(nums[i]>self.minHeap[0]):
                heappop(self.minHeap)
                heappush(self.minHeap,nums[i])
    def add(self, val: int) -> int:
        if(self.k > 0):
            heappush(self.minHeap,val)
            self.k -= 1
        elif(val>self.minHeap[0]):
            heappop(self.minHeap)
            heappush(self.minHeap,val)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)