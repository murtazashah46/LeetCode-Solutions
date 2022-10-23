def merge(a,b):
    c = []
    if(b[0] <= a[1]):
        c.append(b[0])
        c.append(a[1])
    return c

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        answer = []
        for i in range(len(firstList)):
            for j in range(len(secondList)):
                a = min(firstList[i],secondList[j])
                b = max(firstList[i],secondList[j])
                if(b[0] <= a[1]):
                    answer.append([b[0],min(a[1],b[1])])
        return answer