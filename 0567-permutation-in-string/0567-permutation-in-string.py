class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        
        if(len(s1)>len(s2)):
            return False
        dictionary_s1 = {}
        for i in range(97,123):
            dictionary_s1[chr(i)] = 0
        for i in range(len(s1)):
            dictionary_s1[s1[i]] += 1
                
        dictionary = {}
        for i in range(97,123):
            dictionary[chr(i)] = 0
            
        w_start = 0
        substring = ""
        for w_end in range(len(s2)):
            dictionary[s2[w_end]] += 1 
            if(w_end-w_start+1 == len(s1)):
                if(dictionary == dictionary_s1):
                    return True
                dictionary[s2[w_start]] -= 1
                w_start +=1
        return False