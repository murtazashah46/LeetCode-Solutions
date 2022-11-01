import heapq
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