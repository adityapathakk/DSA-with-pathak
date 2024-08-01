# Link to problem: https://www.geeksforgeeks.org/problems/find-pair-given-difference1559/1

class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        arr.sort() # O(N*logN), O(1)
        i, j = 0, 1
        while i < n and j < n:
            diff = arr[j] - arr[i]
            if (diff == x and i != j):
                return 1
            elif diff < x:
                j += 1
            else:
                i += 1
        return -1
        
        # s = set() # O(N), O(N)
        
        # for num in arr:
        #     if (num + x) in s or (num - x) in s:
        #         return 1
        #     s.add(num)
        
        # return -1