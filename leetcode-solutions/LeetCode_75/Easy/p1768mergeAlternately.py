# Problem: 1768. Merge Strings Alternately
# Source: https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75
# Difficulty: Easy
# Summary: You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
#
# Return the merged string.
#
#
#
# Example 1:
#
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:
#
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:
#
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q
# merged: a p b q c   d
#
#
# Constraints:
#
# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.


class Solution(object):
    #
    def mergeAlternately(self, word1, word2):

        """
                :type word1: str
                :type word2: str
                :rtype: str
                """

        merged = []
        if len(word1) == len(word2):
            for i in range(0, len(word1)):
                merged.append(str(word1[i]))
                merged.append(str(word2[i]))
        else:
            pos = 0
            if len(word1) > len(word2):
                for i in range(0, len(word2)):
                    merged.append(str(word1[i]))
                    merged.append(str(word2[i]))
                    pos = i
                merged.append(word1[pos + 1:len(word1)])
            else:
                for i in range(0, len(word1)):
                    merged.append(str(word1[i]))
                    merged.append(str(word2[i]))
                    pos = i
                merged.append(word2[pos + 1:len(word2)])
        merged = ''.join(merged)
        return merged