class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if(len(nums) == 0):
            return -1,-1
        
        left = 0 
        right = len(nums)-1
        while(left < right):
            mid = (left+right)//2
            if(nums[mid] < target):
                left = mid +1
            else:
                right = mid
        
        if(nums[left] != target):
            return -1,-1
        else:
            final_left = left
            left = 0 
            right = len(nums)-1

            while(right >= left):
                mid = (left+right)//2
                if(nums[mid] > target):
                    right = mid-1
                else:
                    left = mid+1

            return final_left,right