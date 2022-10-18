class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if(len(nums) == 1 and nums[0] != target):
            return -1
        elif(len(nums) == 1 and nums[0] == target):
            return 0
        
        left = 0
        right = len(nums)-1
        
        while(nums[left] > target and left < right):
            mid = left + (right-left)//2
            if(nums[mid] == target):
                return mid
            else:
                left += 1
        while(nums[right] < target and left < right):
            mid = left + (right-left)//2
            if(nums[mid] == target):
                return mid
            else:
                right -= 1
                
        while(left <= right):
            mid = left + (right-left)//2
            if(nums[mid] == target):
                return mid
            elif(nums[mid] > target):
                right = mid-1
            elif(nums[mid] < target):
                left = mid+1
        return -1
    