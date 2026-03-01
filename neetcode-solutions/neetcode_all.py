from typing import List

class Solution:

    # Easy

    # Score of a String
    def scoreOfString(self, s: str) -> int:
        i = 0
        res = 0
        while i != len(s) - 1:
            res += abs(ord(s[i]) - ord(s[i + 1]))
            i += 1
        return res

    # Concatenation of Array
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2

    # Contains Duplicate
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = False
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums), 1):
                if nums[i] == nums[j]:
                    duplicate = True
        if not duplicate:
            return False
        else:
            return True

    # Valid Anagram
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            # A brute force solution
            # new_s = list(s)
            # new_s.sort()
            # new_s = str(new_s)
            # new_t = list(t)
            # new_t.sort()
            # new_t = str(new_t)
            # for i in range(len(new_s)):
            #     if new_s[i] != new_t[i]:
            #         return False
            # return True

            # O(1) solution
            for i in range(len(s)):
                if not t.find(s[i], i, len(s)):
                    return False
            return True

    # Replace Elements With Greatest Element On Right Side
    def replaceElements(self, arr: List[int]) -> List[int]:
        j = 1
        res = []
        while len(arr) != j:
            greatest = max(arr[j:len(arr)])
            res.append(greatest)
            j += 1
        res.append(-1)
        return res

    # Is Subsequence
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1  # Only move s pointer if we find a match
            j += 1  # Always move t pointer

        return i == len(s)

    # Length Of Last Word
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(' ')
        res = []
        for word in arr:
            if word != '':
                res.append(word.strip())
        last_word = res[len(res) - 1]
        return len("".join(last_word))

    # Number of Senior Citizens
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(len(details)):
            passenger = details[i]
            if int(passenger[11:13]) > 60:
                count += 1
        return count

    # Two Sum
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums), 1):
                if nums[i] + nums[j] == target and i != j:
                    res.append(i)
                    res.append(j)
        return list(res)

    # Max Consecutive Ones


    # Valid Palindrome
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for char in s:
            if char.isalnum():
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

    # Valid Parentheses
    def isValid(self, s: str) -> bool:
        if not s:
            print("Empty String")
            return True
        arr = []
        for char in s:
            print("CHAR")
            print(char)
            if char in '(':
                arr.append(char)
                print("( ARR")
                print(arr)
            elif char == ')':
                print(") orloo")
                print(not arr)
                print(arr)
                if not arr:
                    print("arr hooson")
                    return False
                top = arr.pop()
                print("TOP")
                print(top)
                if top != '(':
                    print(f"{top} != '('")
                    return False
            elif char in '[':
                arr.append(char)
                print("[ ARR")
                print(arr)
            elif char == ']':
                print("] orloo")
                print(not arr)
                print(arr)
                if not arr:
                    print("arr hooson")
                    return False
                top = arr.pop()
                print("TOP")
                print(top)
                if top != '[':
                    print(f"{top} != '['")
                    return False
            elif char == '{':
                arr.append(char)
                print("{ ARR")
                print(arr)
            elif char == '}':
                print("} orloo")
                print(not arr)
                print(arr)
                if not arr:
                    print("arr hooson")
                    return False
                top = arr.pop()
                print("TOP")
                print(top)
                if top != '{':
                    print(f"{top} != temdeg")
                    return False
        print("len ARR")
        print(len(arr) == 0)
        return len(arr) == 0

    # Medium

    # Group Anagrams
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = []
        # for i in range(len(strs) - 1):
        #     # res.append(strs[i])
        #     res = ''.join(strs[i])
        #     for j in range(i + 1, len(strs), 1):
        #         ana = Solution.isAnagram(self, strs[i], strs[j])
        #         if ana:
        #             res[i].join(strs[j])
        #         else:
        #             res.join(strs[i])
        # # list_of_lists_json = json.loads(res)
        # print(type(res))

        res = []
        visited = [False] * len(strs)

        for i in range(len(strs)):
            if visited[i]:
                continue

            current_group = [strs[i]]
            visited[i] = True

            for j in range(i + 1, len(strs)):
                if not visited[j] and self.isAnagram(strs[i], strs[j]):
                    current_group.append(strs[j])
                    visited[j] = True

            res.append(current_group)
        return res