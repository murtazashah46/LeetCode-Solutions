import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        maxHeap = []
        for i in range(len(points)):
            distance = math.sqrt(points[i][0]**2 + points[i][1]**2)
            if(k > 0):
                heappush(maxHeap,(-distance,i))
                k-=1
            elif(distance < -maxHeap[0][0]):
                heappop(maxHeap)
                heappush(maxHeap,(-distance,i))
        answer = []
        for i in range(len(maxHeap)):
            answer.append(points[maxHeap[i][1]])
        return answer