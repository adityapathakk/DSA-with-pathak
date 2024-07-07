class Solution:
    def check(self, nums: List[int]) -> bool:
       rotateCheck = 0 # if this is greater than 1, it means that the array wasn't sorted.
       length = len(nums)
       for i in range(length):
        if nums[(i + 1) % length] >= nums[i]:
            pass
        else:
            rotateCheck += 1
       if rotateCheck > 1:
        return False
       else:
        return True

''' Approach

a sorted (ascending) array will always have the i + 1 element > i element. in case of rotation, this condition is not met once - i.e. when the element at the end isn't the largest and instead, the next greater value is at the start of the list.
so we check for this unsatisfied condition - if it's broken more than once, then the array isn't sorted, even with rotations.

'''
