class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        if(target >= letters[-1]):
            return letters[0]
        start = 0
        end = len(letters)-1
        mid = start + ((end-start)//2)
        while(start<=end):
            mid = start + ((end-start)//2)
            if(letters[mid] == target):
                found = True
                while(letters[mid] == letters[mid+1]):
                    mid += 1
                return letters[mid+1]
            elif(letters[mid] > target):
                end = mid-1
            elif(letters[mid] < target):
                start = mid+1
        if(target > letters[mid]):
            while(letters[mid] == letters[mid+1]):
                mid += 1
            return letters[mid+1]
        return letters[mid]