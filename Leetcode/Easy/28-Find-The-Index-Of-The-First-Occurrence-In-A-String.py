class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1): # don't iterate through a substring that's shorter than needle
            if haystack[i : i + len(needle)] == needle:
                return i # return the first index of that substring
        return -1 # if loop is exited, then needle isn't part of haystack

# alternative approach - super simple in python, just use
# haystack.find(needle)
