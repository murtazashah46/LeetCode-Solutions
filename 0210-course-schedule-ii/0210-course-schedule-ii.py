class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        prereqs = {}
        for i in range(numCourses):
            prereqs[i] = []
        for course,prereq in prerequisites:
            prereqs[course].append(prereq)
        
        output = []
        visited , cycle = set(), set()
    
        def dfs(course):
            if(course in cycle):
                return False
            if(course in visited):
                return True
            
            cycle.add(course)
            for prereq in prereqs[course]:
                if dfs(prereq) == False:
                    return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True
        
        for course in range(numCourses):
            if(dfs(course) == False):
                return []
        return output
            