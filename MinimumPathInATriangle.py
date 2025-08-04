from typing import List

# class Solution:
#     def numberOfArithmeticSlices(self, nums: List[int]) -> int:
#         n = len(nums)
#         cnt,curr = 0, 0
#         for i in range(n-3,-1,-1):
#             if nums[i+2] - nums[i+1] == nums[i+1]-nums[i]:
#                 curr = 1+curr
#             else:
#                 curr = 0
#             cnt+=curr
#         return cnt


# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         n = len(triangle)
#         memo = [[-1]*n for _ in range(n)]
#         def helper(r,c):
#             # base
#             if r == len(triangle) : return 0
#             if  memo[r][c]!=-1 : return memo[r][c]
#             # logic
#             case0 = helper(r+1, c)+triangle[r][c]
#             case1 = helper(r+1,c+1)+triangle[r][c]
#             memo[r][c] = min(case0, case1)
#             return memo[r][c]
#         return helper(0,0)

# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         n = len(triangle)
#         for i in range(n-2,-1,-1):
#             for j in range(0,i+1,1):
#                 triangle[i][j] = triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])
#         return triangle[0][0]

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(1,n,1):
            for j in range(0,i+1,1):
                if j == 0:
                    triangle[i][j] = triangle[i][j] + triangle[i-1][j]
                elif j == i:
                    triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
                else:
                    triangle[i][j] = triangle[i][j] + min(triangle[i-1][j-1], triangle[i-1][j])
        minval = float("inf")
        for j in range(n):
            minval = min(minval, triangle[n-1][j])
        return minval