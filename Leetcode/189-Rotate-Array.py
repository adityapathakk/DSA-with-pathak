# Approach 1

class Solution(object):
    def rotate(self, nums, k):
        length = len(nums)
        k %= length # avoid unnecessary rotations
        if k != 0: # rotate the array only if required
            end = nums[-k:] # store the elements of the end that will come at the beginning after rotation
            for i in range(length - k - 1, -1, -1): # going backward through first (n - k) elements of the array 
                nums[i + k] = nums[i] # shift each element by k spots
            nums[:k] = end # put the old end to the front

''' Approach 2

the last 'k' elements become the first 'k' elements of the array - reverse the whole list. after that, the first 'k' elements will be the last 'k' elements of our original list, but they will be in reverse order. similarly, the new end of our list will be the old beginning, only in reverse order. reverse the first 'k' elements of our new array and the last 'n - k' elements! after that, the array will be fully rotated!

a reverse function can be made which accepts parameters - start and end. with these indexes, keep swapping their elements - start goes to end and end goes to start. keep updating the pointers.
this reverse function can then be used to carry out the above mentioned approach.

'''
