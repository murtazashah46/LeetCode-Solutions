class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        w_start = 0
        max_sum = -math.inf 
        types = {}
        for w_end in range(len(fruits)):
            types["Type" + str(fruits[w_end])] = types.setdefault("Type" + str(fruits[w_end]), 0) + 1
            while(len(types)>2):
                types["Type" + str(fruits[w_start])] -= 1
                if(types["Type" + str(fruits[w_start])] == 0):
                    types.pop("Type" + str(fruits[w_start]))
                w_start += 1
            max_sum = max(w_end-w_start+1,max_sum)
        return max_sum