
from micro1 import Solution
import ast

s_str = input("Enter: ")
sol = Solution()

# result = sol.reverseWords(s_str)
# print("Result:", result)

s_str = ast.literal_eval(s_str)
result = sol.orderCharDashNumbers(s_str)
for item in result:
    print(item)