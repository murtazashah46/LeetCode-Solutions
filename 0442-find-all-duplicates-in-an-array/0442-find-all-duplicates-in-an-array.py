class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        answer = []
        for i in range(len(nums)):
            while(nums[i] != i+1):
                if(nums[i] == nums[nums[i]-1]):
                    break
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
        
        print(nums)
        for i in range(len(nums)):
            if(nums[i] != i+1):
                answer.append(nums[i])
        return answer