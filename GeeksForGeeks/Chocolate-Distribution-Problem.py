# Link to problem: https://www.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1

class Solution:
    def findMinDiff(self, A,N,M):
        if M > N: return -1 # not enough packets
        A.sort()
        minDiff = 99999999
        for i in range(N - M + 1): # sliding Window
            currDiff = A[i + M - 1] - A[i]
            if currDiff < minDiff: minDiff = currDiff
        return minDiff