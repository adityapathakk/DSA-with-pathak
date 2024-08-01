# Link to problem: https://www.geeksforgeeks.org/problems/permutations-in-array1747/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card

class Solution:
    def isPossible(self,a, b, n, k):
        a.sort(reverse = True)
        b.sort()
        for i in range(n):
            if a[i] + b[i] < k:
                return False
        return True