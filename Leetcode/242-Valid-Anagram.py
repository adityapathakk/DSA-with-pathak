class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = sorted(s), sorted(t)
        return s == t

''' Alternate Approach : Neetcode

this is also a neetcode question: https://neetcode.io/problems/is-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
        
Explanation : https://www.youtube.com/watch?v=9UtInBqnCgA

'''
