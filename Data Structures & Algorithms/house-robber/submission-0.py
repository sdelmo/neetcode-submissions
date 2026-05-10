class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Edge case: not nums, return 0
        if not nums:
            return 0
        
        # Edge case: only one house, return houses value
        if len(nums) == 1:
            return nums[0]
        
        """
        Bottom up DP
        dp = [] such that dp[i] represents max booty at i
        """

        dp = [0] * len(nums)
        # First house booty is just the first house value
        dp[0] = nums[0]
        # Second house max booty would be the max of the first house and the second house
        dp[1] = max(nums[0], nums[1])

        # Iterate over the rest, 2 to the end of nums as we've already populated first two indices
        for i in range(2,len(nums)):
            # The highest booty would be the biggest option of these
            # first param: the max profit at the previous index
            # second: skip previous index (go to i-2) and add current value
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[len(nums)-1]