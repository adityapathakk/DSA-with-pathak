class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        
        return nums

  ''' Approach

left pointer points at the index where the next non-zero element must be placed, and right iterates over the list. while moving the right pointer:
if nums[right] != 0 i.e. nums[right] is a non-zero element: swap a[right] and a[left]. now, the current left is pointing to the non-zero element a[right]. shift the pointer left by 1 so that it can again point to the first zero.

  '''
