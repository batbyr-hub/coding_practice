class Solution(object):

    # Easy

    # 9. Palindrome Number
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        chars = []
        s = str(x)
        for char in s:
            if char.isalnum() or char == '-':
                chars.append(char.lower())
        new_s = "".join(chars)
        half = len(new_s) // 2

        first_half_s = new_s[:half]
        if len(new_s) % 2 != 0:
            second_half_s = new_s[half + 1:]
        else:
            second_half_s = new_s[half:]

        second_half_s = second_half_s[::-1]
        if first_half_s == second_half_s:
            return True
        else:
            return False

    # 20. Valid Parentheses
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