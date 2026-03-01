from neetcode_all import Solution

inp = input("NeetCode: ")
sol = Solution()
listo = inp
# print(listo)
# result = sol.hasDuplicate(listo)
result = sol.isSubsequence(listo)
print("Result:", result)