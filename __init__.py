import ast

from Medium.reverseWords import Solution
from Easy.rounds import SolutionR
inp = ast.literal_eval(input())

# s_str = input("Enter: ")
sol = SolutionR()
# result = sol.reverseWords(s_str)
result = sol.solve(inp)
print("Result:", result)