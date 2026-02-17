# 20. Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 1:
#
# Input: s = "()"
#
# Output: true
#
# Example 2:
#
# Input: s = "()[]{}"
#
# Output: true
#
# Example 3:
#
# Input: s = "(]"
#
# Output: false
#
# Example 4:
#
# Input: s = "([])"
#
# Output: true
#
# Example 5:
#
# Input: s = "([)]"
#
# Output: false
#
#
#
# Constraints:
#
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if s[0] == ')' or s[0] == ']' or s[0] == '}':
            return False
        else:
            stack = []
            for i in range(len(s)):
                if s[i] == '(':
                    stack.append(s[i])
                if s[i] == ')':
                    if not stack:
                        return False
                    top = stack.pop()
                    if top != '(':
                        return False
                if s[i] == '[':
                    stack.append(s[i])
                if s[i] == ']':
                    if not stack:
                        return False
                    top = stack.pop()
                    if top != '[':
                        return False
                if s[i] == '{':
                    stack.append(s[i])
                if s[i] == '}':
                    if not stack:
                        return False
                    top = stack.pop()
                    if top != '{':
                        return False

            stack = ''.join(stack)
            # print("stack: " + str(stack))
            if len(stack) == 0:
                return True
            return False
