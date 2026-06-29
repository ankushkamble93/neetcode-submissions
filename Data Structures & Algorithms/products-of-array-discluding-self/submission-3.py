class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dp = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            dp[i] *= prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            dp[i] *= postfix
            postfix *= nums[i]
        return dp