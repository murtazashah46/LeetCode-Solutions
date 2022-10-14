class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        k_count = k
        for i in range(1,max(arr)+k+1):
            if(i not in arr):
                k_count -= 1
            if(k_count == 0):
                return i