class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0]) 

        rowMin = []
        for i in range(m):
            Min = 9999999999
            for j in range(n):
                Min = min(Min, matrix[i][j])
            rowMin.append(Min)

        colMax = []
        for i in range(n):
            Max = -1
            for j in range(m):
                Max = max(Max, matrix[j][i])
            colMax.append(Max)

        lucky = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == rowMin[i] and matrix[i][j] == colMax[j]:
                    lucky.append(matrix[i][j])
        
        return lucky

''' Approach

find minimum of each row, put in Min
find maximum of each column, put in Max
find the number that occurs in both Min and Max - that's the answer.

'''
