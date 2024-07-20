class Solution: # Greedy Approach (inspired by Editorial)
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        N = len(rowSum)
        M = len(colSum)

        currRowSum = [0] * N
        currColSum = [0] * M

        originalMatrix = [[0] * M for _ in range(N)]

        for i in range(N):
            for j in range(M):
                originalMatrix[i][j] = min(rowSum[i] - currRowSum[i], colSum[j] - currColSum[j])
                currRowSum[i] += originalMatrix[i][j]
                currColSum[j] += originalMatrix[i][j]
        
        return originalMatrix

''' Approach

Imagine there is a non-negative integer matrix origMatrix with dimensions N×M. We have performed a sum operation on each row and column of the matrix, storing the results in two lists: rowSum and colSum. The list rowSum of size N contains the sum of each row of the original matrix, while the list colSum of size M contains the sum of each column. Given these two lists, rowSum and colSum, we need to reconstruct the original matrix origMatrix. The inputs are guaranteed to be valid, meaning at least one solution exists, and any valid matrix can be returned in the case of multiple solutions.

Let's think about the value we can assign to a particular cell at row r and column c. We need to assign such a value that the total sum in the row doesn't exceed rowSum[r] and total sum in the column doesn't exceed colSum[c]. This is because we can only have non-negative integers in the matrix and hence we cannot exceed the total sum. We can greedily choose the maximum number we can assign to a cell and what should it be? The maximum value we can assign considering only the rows will be rowSum[r] - sum of all cells we have filled in row r so far, similarly the maximum value we can assign considering only the columns will be colSum[c] - sum of all cells we have filled in the column c so far. As just discussed we cannot exceed the total sum in any of the two constraints (row and column) we will choose the minimum of these two values to assign to the cell at (r, c).

To achieve this, we iterate over the elements of the matrix, maintaining the cumulative sums of the rows and columns processed so far. Let currRowSum[i] represent the sum of the elements in the i-th row up to the current element, and currColSum[j] represent the sum of the elements in the j-th column up to the current element. For the cell (i, j), the value can be determined as:

K=min(rowSum[i]−currRowSum[i],colSum[j]−currColSum[j])

This ensures that the sum of the i-th row does not exceed rowSum[i] and the sum of the j-th column does not exceed colSum[j]. After determining K, we update currRowSum[i] and currColSum[j] by adding K.

We initialize currRowSum and currColSum to zero and proceed from the top left to the bottom right of the matrix, filling in the values and storing them in origMatrix.

'''

''' Space Optimised Greedy

class Solution:
    def restoreMatrix(self, rowSum, colSum):
        # Get the dimensions of the matrix
        rows = len(rowSum)
        cols = len(colSum)
        
        # Initialize the matrix with zeros
        matrix = [[0] * cols for _ in range(rows)]
        
        # Iterate through each cell in the matrix
        for i in range(rows):
            for j in range(cols):
                # Determine the value for matrix[i][j]
                val = min(rowSum[i], colSum[j])
                
                # Place the value in the matrix
                matrix[i][j] = val
                
                # Update the row and column sums
                rowSum[i] -= val
                colSum[j] -= val
        
        return matrix

'''
