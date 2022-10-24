class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        w_start = 0
        count = 0
        avg = 0
        summation = 0
        for w_end in range(len(arr)):
            summation += arr[w_end]
            
            if(w_end-w_start+1 == k):
                if(summation/k >= threshold):
                    count += 1
                summation -= arr[w_start]
                w_start += 1
        return count