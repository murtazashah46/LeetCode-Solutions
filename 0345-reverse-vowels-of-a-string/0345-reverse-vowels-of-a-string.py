class Solution:
    def reverseVowels(self, s: str) -> str:
        
        start = 0
        end = len(s)-1
        s = list(s)
        
        while(start < end):
            if(s[start] not in "aeiouAEIOU"):
                start += 1
                
            if(s[end] not in "aeiouAEIOU"):
                end -= 1
            
            if(s[start] in "aeiouAEIOU" and s[end] in "aeiouAEIOU"):
                temp = s[start]
                s[start] = s[end]
                s[end] = temp
                start+= 1
                end-= 1 
        return "".join(s)