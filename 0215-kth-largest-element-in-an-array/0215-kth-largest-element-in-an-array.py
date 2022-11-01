class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        s = sorted(nums,reverse=True)
        return s[k-1]