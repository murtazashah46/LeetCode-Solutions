from collections import Counter
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        
        dictionary = Counter(s)
        
        minHeap = []
        for element in dictionary:
            heappush(minHeap,dictionary[element])
        s = ""
        while(minHeap):
            freq = heappop(minHeap)
            letter = [i for i in dictionary if dictionary[i]==freq]
            s += letter[0]*freq
            dictionary.pop(letter[0])
        return s[::-1]