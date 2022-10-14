def merge(a,b):
    c = []
    if(b[0] <= a[1]):
        c.append(a[0])
        c.append(max(a[1],b[1]))
    return c

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        inserted = False
        for i in range(len(intervals)):
            if(intervals[i][0]>=newInterval[0]):
                intervals.insert(i,newInterval)
                inserted = True
                break
        if(inserted == False):
            intervals.append(newInterval)
        
        i = 0
        while(i < len(intervals)-1):
            c = merge(intervals[i],intervals[i+1])
            if(c != []):
                intervals.pop(i)
                intervals.pop(i)
                intervals.insert(i,c)
            else:
                i += 1
        return intervals