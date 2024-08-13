class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        firstRowHasZero, firstColHasZero = False, False

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0: firstRowHasZero = True
                    if col == 0: firstColHasZero = True
                    matrix[row][0] = matrix[0][col] = 0
        
        for row in range(1, m):
            for col in range(1, n):
                if matrix[0][col] == 0 or matrix[row][0] == 0: matrix[row][col] = 0
            
        if firstRowHasZero:
            for col in range(n): matrix[0][col] = 0
        
        if firstColHasZero:
            for row in range(m): matrix[row][0] = 0