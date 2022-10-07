def merge(a,b):
    c = []
    if(b[0] <= a[1]):
        c.append(a[0])
        c.append(max(a[1],b[1]))
    return c

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 0
        intervals = sorted(intervals)
        while(i < len(intervals)-1):
            c = merge(intervals[i],intervals[i+1])
            if(c != []):
                intervals.pop(i)
                intervals.pop(i)
                intervals.insert(i,c)
            else:
                i += 1
        return intervals