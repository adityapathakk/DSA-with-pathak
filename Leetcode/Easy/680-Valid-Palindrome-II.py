class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0 # first pointer, starting from beginning of string
        right = len(s) - 1 # second pointer, starting from end of string
        
        while left < right: # index should be less then right one, as  we dont need to compare the same index
            if s[left] == s[right]: # if both the values are equal
                left += 1 # if yes increase them both
                right -= 1
            else: # if not, we check if it is after removing either right or left value
                return s[left:right] == s[left:right][::-1] or s[left+1:right+1] == s[left+1:right+1][::-1] # return true if either situation is true.
        
        return True # true as all values are the same. 