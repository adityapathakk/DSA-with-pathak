class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # defining helper function to remove substrings
        def removeSubStr(s, firstChar, secondChar, points):
            stack, score = [], 0
            for char in s:
                if stack and stack[-1] == firstChar and char == secondChar:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)
            return ''.join(stack), score

        if x > y: # remove 'ab' first
            s, score1 = removeSubStr(s, 'a', 'b', x)
            s, score2 = removeSubStr(s, 'b', 'a', y)
        else: # remove 'ba' first
            s, score1 = removeSubStr(s, 'b', 'a', y)
            s, score2 = removeSubStr(s, 'a', 'b', x)

        return score1 + score2

''' Approach

two things to note here:

we need to determine how to maximise our points. that can be done by FIRST removing the substrings which're worth more points, and then removing the the substring which is worth less points.
for example, if x > y, then 'ab' is worth more points, and we should remove that first to maximise the points.

using a stack, we can keep track of the last 2 characters when we iterate over the given string. when the for loop reaches a character (say, i) of the string, we check if the last element in
the stack (i - 1) is the first character of the substring, and the current iteration's character (i) is the second character of the substring.

    -> if that's the case, then we pop the last element of the stack and don't add the current iteration's character to the stack. substring removed, points gained!
    -> otherwise, add the current iteration's character (i) to the stack.

'''
