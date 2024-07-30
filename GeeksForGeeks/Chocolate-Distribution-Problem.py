class Solution:
    def findMinDiff(self, A,N,M):
        if M > N: return -1 # Not enough packets
        A.sort()
        minDiff = 99999999
        for i in range(N - M + 1): # Sliding Window
            currDiff = A[i + M - 1] - A[i]
            if currDiff < minDiff: minDiff = currDiff
        return minDiff