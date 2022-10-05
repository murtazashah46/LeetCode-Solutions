class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        array = [[1],[1,1]]
        for i in range(2,rowIndex+1):
            new_row = []
            new_row.append(1)
            for j in range(1,i):
                new_row.append(array[i-1][j]+array[i-1][j-1])
            new_row.append(1)
            array.append(new_row)
        return array[rowIndex]