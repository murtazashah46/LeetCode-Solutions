class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subsets.append([])
        
        for number in (nums):
            n = len(subsets)
            for j in range(n):
                temp_set = list(subsets[j])
                temp_set.append(number)
                if(sorted(temp_set) not in subsets):
                    subsets.append(sorted(temp_set))
        return subsets