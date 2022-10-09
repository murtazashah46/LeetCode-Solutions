class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)
        w_start = 0
        summation = 0
        max_same = -math.inf
        for w_end in range(len(nums)):
            summation += nums[w_end]
            while(nums[w_end] * (w_end-w_start+1) > summation + k):
                summation -= nums[w_start]
                w_start += 1
            max_same=max(max_same,w_end-w_start+1)
        return max_same
