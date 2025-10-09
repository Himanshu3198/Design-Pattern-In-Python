class Solution(object):
    def memo(self, nums, dp, i):
        if i >= len(nums):
            return 0
        if i in dp:
            return dp[i]
        ans = 0
        op1 = nums[i] + self.memo(nums, dp, i + 2)
        op2 = self.memo(nums, dp, i + 1)
        ans = max(op1, op2)
        dp[i] = ans

        return ans

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {}
        return self.memo(nums, dp, 0)
