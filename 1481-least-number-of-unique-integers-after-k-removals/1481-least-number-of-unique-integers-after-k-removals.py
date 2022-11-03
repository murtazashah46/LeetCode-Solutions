from collections import Counter
import heapq
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        dictionary = Counter(arr)
        minHeap = []
        for element in dictionary:
            heappush(minHeap,dictionary[element])
        while(k > 0):
            if(minHeap[0] <= k):
                freq = heappop(minHeap)
                k -= freq
            else:
                break
        return len(minHeap)
        