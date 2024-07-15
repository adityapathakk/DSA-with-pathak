class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seenSet = set() # set that contains each number from nums (only once)

        for i in (nums): 
            
            if i in seenSet:
                return True # if list already contains the number, then it's a duplicate

            seenSet.add(i) # append the number that we're seeing for the first time to the list
        
        return False

  # this is also a neetcode question: https://neetcode.io/problems/duplicate-integer
