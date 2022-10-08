class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        s_nums = sorted(nums)
        
        start = 0
        end = len(nums)-1
        s_changed = False
        e_changed = False
        while(start < end):
            if(nums[start] != s_nums[start] and s_changed == False):
                s_changed = True
            elif(s_changed == False):
                start += 1
            
            if(nums[end] != s_nums[end] and e_changed == False):
                e_changed = True
            elif(e_changed == False):
                end -= 1
                
            if(s_changed == True and e_changed == True):
                break
        
        if(s_changed == False and e_changed == False):
            return 0
        return end - start +1