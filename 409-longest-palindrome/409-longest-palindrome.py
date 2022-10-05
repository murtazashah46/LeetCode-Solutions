class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = 0
        one_count = False
        set_s = set(s)
        for elem in set_s:
            if(s.count(elem)%2 == 0):
                counter += s.count(elem)
            else:
                counter += s.count(elem)-1
                one_count = True
        if(one_count == True):
            return counter+1
        return counter