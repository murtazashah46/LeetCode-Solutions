class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        temp = []
        answer = []
        nums = sorted(nums)
        for i in range(len(nums)-1):
            start = i+1
            end = len(nums)-1
            while(start < end):
                summation = nums[start]+nums[end]+nums[i]
                if(summation == 0):
                    answer.append((nums[start],nums[i],nums[end]))
                    start += 1
                    end -= 1
                elif(summation < 0):
                    start += 1
                else:
                    end -= 1
        return set(answer)