from typing import List


class Solution:
    def hasduplicateeee(self, nums: List[int]) -> bool:
        duplicate = False
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums), 1):
                if nums[i] == nums[j]:
                    duplicate = True
        if not duplicate:
            return False
        else:
            return True

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if not t.find(s[i], i, len(s)):

                    return False
            return True