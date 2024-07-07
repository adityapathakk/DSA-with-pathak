class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
# whenever j and i aren't equal, it means a unique element is found. so length of unique elements' list increases.
                nums[j] = nums[i]
        
        return j + 1 # j began from the 0th index.

''' Approach

used a two-pointer approach. using a for loop, i compare the j element (starting from index 0) with i element (starting from index 1).
if the elements aren't equal, that means we've found a unique number. so we can add one to the length of unique elements in the list.
if they are equal, then we move on to the next iteration, until we find another unique element. these unique elements keep getting added to the list, changing it in-place.

'''

''' Alternate Solution

also, we could simply use the property of lists:
        #nums[:] = sorted(set(nums))
        #return len(nums)
        
'''
