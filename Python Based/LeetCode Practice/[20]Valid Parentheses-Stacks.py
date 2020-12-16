# Initialize a stack S.
# Process each bracket of the expression one at a time. If we encounter an opening bracket,
# we simply push it onto the stack. This means we will process it later, let us simply move onto the sub-expression
# ahead.
# If we encounter a closing bracket, then we check the element on top of the stack.
# If the element at the top
# of the stack is an opening bracket of the same type, then we pop it off the stack and continue processing.
# Else,
# this implies an invalid expression.
# In the end, if we are left with a stack still having elements,
# then this implies an invalid expression.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'

                if mapping[char] != top_element:
                    return false
            else:
                stack.append(char)

        return not stack

