class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        summation = (N * (N + 1)) // 2
        sumNums = sum(nums)
        
        return summation - sumNums

''' Approach

(sum of N numbers formula) - (sum of N numbers with one number missing) = (that missing number)

'''

''' Another optimal approach

XOR something with 0, returns the same number. XOR 2 same numbers, returns 0. XOR 2 different numbers, no result.

XOR all numbers from 1 to N, store as x
XOR all numbers in the array, store as y
XOR x and y.

'''
