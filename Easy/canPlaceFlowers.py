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

        # for i in range(len(flowerbed)):
        #     if i - 1 > -1:
        #         if flowerbed[i - 1] == 0:
        #             if flowerbed[i] == 0:
        #                 if i + 1 < len(flowerbed):
        #                     if flowerbed[i + 1] == 0:
        #                         n -= 1
        #                         flowerbed[i] = 1
        #                 else:
        #                     n -= 1
        #                     flowerbed[i] = 1
        #     else:
        #         if flowerbed[i] == 0:
        #             if i + 1 < len(flowerbed):
        #                 if flowerbed[i + 1] == 0:
        #                     n -= 1
        #                     flowerbed[i] = 1
        #             else:
        #                 n -= 1
        #                 flowerbed[i] = 1
        #         else:
        #
        #     if n < 1:
        #         break
        # return True

        # arr = self.countNotEmpty(flowerbed)
        # removed_count = self.possibleMax(arr)
        #
        # if removed_count >= n:
        #     return True
        # else:
        #     return False

        count = 0
        for i in range(len(flowerbed)):
            if (flowerbed[i] == 0 and
                    (i == 0 or flowerbed[i - 1] == 0) and
                    (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)):
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
        return count >= n

    # def countNotEmpty(self, flowerbed):
    #     arr = []
    #     for i in range(len(flowerbed)):
    #         if flowerbed[i] == 0:
    #             arr.append(i)
    #     return arr
    #
    # def possibleMax(self, arr):
    #     # slot = []
    #     print("original arr:", arr)
    #     count = 0
    #     for i in range(1, len(arr)):
    #         print("Checking index:", i)
    #         print("arr in for-loop:", arr)
    #         if i + 1 < len(arr):
    #             if arr[i] - 1 == arr[i - 1] and arr[i] + 1 == arr[i + 1]:
    #
    #                 # slot.append(arr[i])
    #                 arr.remove(i)
    #                 print(f"arr after removed index {i}:", arr)
    #                 count += 1
    #     return count

flowerbed_str = input("Enter the flowerbed array (e.g., [1,0,0,0,0,1]): ")
flowerbed = eval(flowerbed_str)   # converts string "[1,0,0,0,1]" → [1,0,0,0,1]

n = int(input("Enter the number of flowers to plant: "))

sol = Solution()
result = sol.canPlaceFlowers(flowerbed, n)
print("Result:", result)