# Problem: 605. Can Place Flowers
# Source: https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75
# Difficulty: Easy
# Summary: You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
#
#
#
# Example 1:
#
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:
#
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
#
#
# Constraints:
#
# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length


class Solution(object):

    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        for i in range(len(flowerbed)):
            if i - 1 > -1:
                if flowerbed[i - 1] == 0:
                    if flowerbed[i] == 0:
                        if i + 1 < len(flowerbed):
                            if flowerbed[i + 1] == 0:
                                n -= 1
                                flowerbed[i] = 1
                        else:
                            n -= 1
                            flowerbed[i] = 1
            else:
                if flowerbed[i] == 0:
                    if i + 1 < len(flowerbed):
                        if flowerbed[i + 1] == 0:
                            n -= 1
                            flowerbed[i] = 1
                    else:
                        n -= 1
                        flowerbed[i] = 1
                else:

            if n < 1:
                break
        return True