class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        
        for i in range(len(arr)):
            if(arr[i] in freq):
                freq[arr[i]] += 1
            else:
                freq[arr[i]] = 1
        
        f_array = []
        for element in freq:
            if(freq[element] in f_array):
                return False
            f_array.append(freq[element])
        return True
    
        