class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        arr = []
        start = 0
        last = len(nums)-1
        
        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]
        
        
        
        while(start <= last):
            if(nums[last] >= nums[start]):
                arr.insert(0,nums[last])
                last -= 1
            elif(nums[last] < nums[start]):
                arr.insert(0,nums[start])
                start += 1
        return arr