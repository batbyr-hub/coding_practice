class Solution(object):

    # Easy

    # 1768. Merge Strings Alternately
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

    # 1071. Greatest Common Divisor of Strings
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        # if str1 + str2 != str2 + str1:
        #     return ""

        # shorter_base = str2
        # if len(str1) < len(str2):
        #     shorter_base = str1
        # real_base_len = len(str1) - len(str2)
        # len1, len2 = len(str1), len(str2)
        # n1, n2 = len1 // real_base_len, len2 // real_base_len
        # base = shorter_base[:real_base_len]

        # if str1 == n1 * base and str2 == n2 * base:
        #     return base

        len1, len2 = len(str1), len(str2)

        def valid(k):
            if len1 % k or len2 % k:
                return False
            n1, n2 = len1 // k, len2 // k
            base = str1[:k]
            return str1 == n1 * base and str2 == n2 * base

        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
        return ""

        # if str1 + str2 != str2 + str1:
        #     return ""

        # max_length = len(str1) #9
        # shorter_base = str2 #ABCABC
        # if len(str1) < len(str2):
        #     shorter_base = str1
        # # while len(str1)
        # shorter_base = shorter_base[:-1]
        # temp_base = str1[:max_length - len(shorter_base) - 1]
        # return temp_base

    # def get_base(str1, str2):

    # # shorter_base = base
    # # if str1.find(base) != -1:
    # return len(base)

    # else:
    # if str1.find(str2) != -1:
    #     sub_str2 = str2[0:len(str2) / 2]
    #     if self.gcdOfStrings(str2, sub_str2) != "":
    #         return sub_str2
    #     return str2
    # else:
    #     return ""

    # 1431. Kids With the Greatest Number of Candies
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max = candies[0]
        for i in range(1, len(candies)):
            # for j in range(i + 1, len(candies) - 1):
            if max < candies[i]:
                max = candies[i]
        res = []
        for j in range(len(candies)):
            if candies[j] + extraCandies >= max:
                res.append(True)
            else:
                res.append(False)
        return res

    # 605. Can Place Flowers
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        arr = self.countNotEmpty(flowerbed)
        # slot = self.possibleMax(arr)
        slot = []
        i_arr = []
        for i in range(1, len(arr)):
            i_arr.append(i)
            if i + 1 < len(arr):
                if arr[i] - 1 == arr[i - 1] and arr[i] + 1 == arr[i + 1]:
                    slot.append(arr[i])
                    i += 1
        return i_arr

        if len(slot) >= n:
            return True
        else:
            return False

    def countNotEmpty(self, flowerbed):
        arr = []
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                arr.append(i)
        return arr

    def possibleMax(self, arr):
        slot = []
        for i in range(1, len(arr)):
            if i + 1 < len(arr):
                if arr[i] - 1 == arr[i - 1] and arr[i] + 1 == arr[i + 1]:
                    slot.append(arr[i])
                    i += 1
        return slot

    # 345. Reverse Vowels of a String
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        arr = []
        for i in range(len(s) - 1, -1, -1):
            if (s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or
                    s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U'):
                arr.append(s[i])
        for i in range(len(s)):
            if (s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or
                    s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U'):
                s[i] = arr[0]
                arr.remove(arr[0])
        return ''.join(s)

    # Medium

    # 151. Reverse Words in a String
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        arr = []
        for i in range(len(s) - 1, -1, -1):
            arr.append(s[i])
        return ' '.join(arr)