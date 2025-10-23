
from micro1 import Solution
from xAI import Solution
import ast

inp = input()
sol = Solution()

# result = sol.reverseWords(inp)
# print("Result:", result)

inp_list = ast.literal_eval(inp)
# result = sol.orderCharDashNumbers(inp_list)
# result = sol.matrixBoard(inp)

for i in range(len(inp_list) - 1, 0, -1):
    print("ROW")
    print(i)
    for j in range(len(inp_list)):
        print("COL")
        print(j)
        print(inp_list[j])
        # if board[i][j] == '*':
        #     board[i][j] = '-'
        print(inp_list[i][j])

# for item in result:
#     print(item)