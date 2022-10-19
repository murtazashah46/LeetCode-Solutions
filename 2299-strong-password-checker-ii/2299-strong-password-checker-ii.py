import string
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        lowerc = False
        upperc = False
        digitc = False
        specialc = False
        
        if(len(password) < 8):
            return False
        
        for i in range(len(password)):
            if(i != len(password)-1):
                if(password[i] == password[i+1]):
                    return False
            if(password[i] in lower):
                lowerc = True
            if(password[i] in upper):
                upperc = True
            if(password[i] in "0123456789"):
                digitc = True
            if(password[i] in "!@#$%^&*()-+"):
                specialc = True
        if(lowerc and upperc and digitc and specialc):
            return True
        return False