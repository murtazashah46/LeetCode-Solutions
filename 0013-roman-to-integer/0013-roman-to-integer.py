class Solution:
    def romanToInt(self, s: str) -> int:
        
        dictionary = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        
        summation = 0
        i = 0 
        while(i<len(s)):
            print(summation)
            if(i < len(s)-1 and s[i] == 'I' and s[i+1] == "V"):
                summation += 4
                i += 2
            elif(i < len(s)-1 and s[i] == 'I' and s[i+1] == "X"):
                summation += 9
                i += 2
            elif(i < len(s)-1 and s[i] == 'X' and s[i+1] == "L"):
                summation += 40
                i += 2
            elif(i < len(s)-1 and s[i] == 'X' and s[i+1] == "C"):
                summation += 90
                i += 2
            elif(i < len(s)-1 and s[i] == 'C' and s[i+1] == "D"):
                summation += 400
                i += 2
            elif(i < len(s)-1 and s[i] == 'C' and s[i+1] == "M"):
                summation += 900
                i += 2
            else:
                summation += dictionary[s[i]]
                i += 1
        return summation