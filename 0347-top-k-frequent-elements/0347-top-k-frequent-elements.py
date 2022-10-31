import heapq
class MedianFinder:
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

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dictionary = {}
        for num in nums:
            dictionary[num] = dictionary.setdefault(num, 0) + 1
        minHeap = []
        for element in dictionary:
            if(k > 0):
                heappush(minHeap, dictionary[element])
                k -= 1
            elif(dictionary[element] > minHeap[0]):
                heappop(minHeap)
                heappush(minHeap,dictionary[element])
        answer = [element for element,freq in dictionary.items() if freq in minHeap]
        return answer