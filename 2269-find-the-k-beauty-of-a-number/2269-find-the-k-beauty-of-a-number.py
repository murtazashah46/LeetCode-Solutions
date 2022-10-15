class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        w_start = 0
        string_num = str(num)
        number = ""
        k_beauty = 0
        for w_end in range(len(string_num)):
            number += string_num[w_end]
            
            if(w_end-w_start+1 == k):
                if(int(number) != 0 and num%int(number) == 0):
                    k_beauty += 1
                number = number[1:]
                w_start += 1
        return k_beauty