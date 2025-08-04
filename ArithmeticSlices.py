from typing import List
# class Solution:
#     def numberOfArithmeticSlices(self, nums: List[int]) -> int:
#         cnt = 0
#         n = len(nums)
#         for i in range(0,n-2):
#             diff = nums[i+1] -nums[i]
#             for j in range(i+2,n):
#                 if nums[j]-nums[j-1] == diff:
#                     cnt+=1
#                 else:
#                     break
#         return cnt


# class Solution:
#     def numberOfArithmeticSlices(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [0]*n
#         for i in range(2,n):
#             if nums[i] - nums[i-1] == nums[i-1] -nums[i-2]:
#                 dp[i] = 1+dp[i-1]
#             else:
#                 dp[i] = 0
#         return sum(dp) 

# class Solution:
#     def numberOfArithmeticSlices(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [0]*n
#         for i in range(n-3,-1,-1):
#             if nums[i+2] - nums[i+1] == nums[i+1]-nums[i]:
#                 dp[i] = 1+dp[i+1]
#             else:
#                 dp[i] = 0
#         return sum(dp) 

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        cnt,curr = 0, 0
        for i in range(n-3,-1,-1):
            if nums[i+2] - nums[i+1] == nums[i+1]-nums[i]:
                curr = 1+curr
            else:
                curr = 0
            cnt+=curr
        return cnt

        

        
        