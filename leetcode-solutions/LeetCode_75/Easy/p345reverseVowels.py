# 345. Reverse Vowels of a String

# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
#
#
#
# Example 1:
#
# Input: s = "IceCreAm"
#
# Output: "AceCreIm"
#
# Explanation:
#
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
#
# Example 2:
#
# Input: s = "leetcode"
#
# Output: "leotcede"
#
#
#
# Constraints:
#
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

class SolutionreverseVowels(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        print(s)
        print(type(s))
        s = list(s)
        print(s)

        arr = []
        for i in range(len(s) - 1, -1, -1):
            if (s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or
                    s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U'):
                arr.append(s[i])
        print(arr)
        for i in range(len(s)):
            if (s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or
                    s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U'):
                s[i] = arr[0]
                print(s)
                arr.remove(arr[0])
                print(arr)
        return ''.join(s)
