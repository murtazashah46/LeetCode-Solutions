import heapq
class Solution:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []        
    def addNum(self, num: int) -> None:
        if(not self.maxHeap or -self.maxHeap[0] >= num):
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)
        
        if(len(self.maxHeap) > len(self.minHeap) + 1):
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif(len(self.maxHeap) < len(self.minHeap)):
            heappush(self.maxHeap, -heappop(self.minHeap))
            
    def findMedian(self) -> float:
        if(len(self.minHeap) == len(self.maxHeap)):
            return -self.maxHeap[0]/2 + self.minHeap[0]/2
        else:
            return -self.maxHeap[0] / 1
    def removeNum(self,number) -> None:
        if(number in self.minHeap):
            self.minHeap.pop(self.minHeap.index(number))
            heapify(self.minHeap)
        else:
            self.maxHeap.pop(self.maxHeap.index(-number))
            heapify(self.maxHeap)
            
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        answer = []
        w_start = 0
        for w_end in range(len(nums)):
            self.addNum(nums[w_end])
            if(w_end-w_start+1 == k):
                answer.append(self.findMedian())
                self.removeNum(nums[w_start])
                w_start += 1
        return answer