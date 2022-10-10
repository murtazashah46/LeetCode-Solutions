class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            while(nums[i] != i):
                if(nums[i] > len(nums)-1):
                    break
                temp = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = temp
        for i in range(len(nums)):
            if(nums[i] != i):
                return i
        return len(nums)