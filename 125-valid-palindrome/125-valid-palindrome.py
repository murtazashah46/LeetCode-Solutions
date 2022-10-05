class Solution:
    def isPalindrome(self, s: str) -> bool:
        for char in s:
            if(char.isalnum() != True):
                s = s.replace(char,"")
        s = s.lower()
        print(s)
        if(s == s[::-1]):
            return True
        return False