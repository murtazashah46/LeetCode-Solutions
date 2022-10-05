class Solution:
    def isValid(self, s: str) -> bool:
        
        if(len(s)%2 != 0):
            return False
        
        opening = "([{"
        stack = []
        for brac in s:
            if(brac in opening):
                stack.append(brac)
            else:
                if(len(stack) == 0):
                    return False
                if(len(stack) == 0 or brac == ")" and stack.pop(-1) != "(" or brac == "]" and stack.pop(-1) != "[" or brac == "}" and stack.pop(-1) != "{"):
                    return False

        if(len(stack) != 0):
            return False
        return True