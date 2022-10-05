class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        answer = []
        for number in nums:
            if(number%2 == 0):
                answer.insert(0,number)
            else:
                answer.append(number)
        return answer