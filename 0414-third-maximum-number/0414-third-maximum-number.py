class Solution:
    def thirdMax(self, nums: List[int]) -> int:
    
        nums = list(set(nums))
        if(len(nums) < 3):
            return max(nums)
        
        for i in range(3):
            answer = max(nums)
            nums.pop(nums.index(answer))
        return answer