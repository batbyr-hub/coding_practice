from typing import List

class Solution:
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

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            new_s = list(s)
            new_s.sort()
            new_s = str(new_s)
            new_t = list(t)
            new_t.sort()
            new_t = str(new_t)
            for i in range(len(new_s)):
                if new_s[i] != new_t[i]:
                    return False
            return True