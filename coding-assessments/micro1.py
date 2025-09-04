class Solution(object):

    def orderCharDashNumbers(self, s_str):

        # ["asd-123", "abc-012", "sdf-001"]

        chars = []
        nums = []
        dashes = []

        for i in range(len(s_str)):
            chars.append(s_str[i].split('-')[0])
            if '-' in s_str[i]:
                dashes.append('-')
            nums.append(s_str[i].split('-')[1])

        # Sort alphabetic characters case-insensitively
        chars.sort()
        # Sort numeric characters
        nums.sort()

        res = []
        for i in range(len(chars)):
            # Concatenate the sorted lists
            res.append(''.join(chars[i] + dashes[i] + nums[i]))

        return res
