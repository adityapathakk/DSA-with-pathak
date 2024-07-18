class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numZeroes = numOnes = numTwos = 0

        for i in nums:
            if i == 0:
                numZeroes += 1
            elif i == 1:
                numOnes += 1
            else:
                numTwos += 1
        
        nums[:] = [0] * numZeroes + [1] * numOnes + [2] * numTwos
        # uncomment if you want to learn how arrays work in Python ->
        # nums = [0] * numZeroes + [1] * numOnes + [2] * numTwos

''' Approach

a simple idea that comes to mind is count the number of 0s, 1s and 2s, and then fill nums with the respective counts of 0s, 1s and 2s.
O(N) time, O(1) space.
leetcode solutions post link: https://leetcode.com/problems/sort-colors/solutions/5496488/extremely-simple-and-efficient-approach-beginners-check-this-out/

'''
