class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if(len(word) == 1):
            return True
        if(ord(word[0])>= 65 and ord(word[0])<=91):
            print("here")
            if(ord(word[1])>= 65 and ord(word[1])<=91):
                print("here2")
                for i in range(2,len(word)):
                    if(ord(word[i]) >= 97 and ord(word[i])<=123):
                        return False
            else:
                for i in range(2,len(word)):
                    if(ord(word[i])>= 65 and ord(word[i])<=91):
                        return False
                
        else:
            for i in range(1,len(word)):
                if(ord(word[i])>= 65 and ord(word[i])<=91):
                    return False

        return True