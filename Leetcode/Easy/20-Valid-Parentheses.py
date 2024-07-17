class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if stack:
                last = stack[-1]
                if last == "(" and i == ")" or last == "[" and i == "]" or last == "{" and i == "}":
                    stack.pop()
                    continue
            stack.append(i)
        
        return not stack

# beat 99.3% (time), 98.6% (space)      
# leetcode solution post link: https://leetcode.com/problems/valid-parentheses/solutions/5493446/easiest-approach-with-stack-beats-99-3-time-98-6-space/
