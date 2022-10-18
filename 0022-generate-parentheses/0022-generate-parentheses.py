def generateP(answer,s,left,right):
    if(left==0 and right == 0):
        answer.append(s)
    if(left>0):
        generateP(answer,s+"(",left-1,right)
    if(right>0 and left<right):
        generateP(answer,s+")",left,right-1)
        
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        generateP(answer,"",n,n)
        return answer