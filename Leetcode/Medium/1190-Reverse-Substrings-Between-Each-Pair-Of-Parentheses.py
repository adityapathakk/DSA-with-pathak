class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ")":
                reverse = ""
                while stack[-1] != "(": # until we encounter an opening bracket...
                    reverse += stack.pop() #... pop everything from the stack, add it to 'reverse'.
                if stack:
                    stack.pop() # pop the opening bracket 
                for ch in reverse:
                    stack.append(ch) # add the reversed substring back to the stack
            else:
                stack.append(char)
        
        return ''.join(stack)

''' Approach

using a stack data structure to keep track of the characters and more importantly, the parentheses.
no matter how many opening brackets '(' we encounter, the first closing bracket ')' we see means that we have found an inner substring.

therefore, whenever we see a ')', a blank string `reverse` is initialised. we keep popping the last character (hence, we obtain a reversed string) from the stack and add it to `reverse`. this process is stopped when we reach a '(', i.e. the parentheses match and the inner substring has been reversed. the reversed substring is added back to the stack, and we continue to look for the next ')', until we're done with the entire string.

'''
