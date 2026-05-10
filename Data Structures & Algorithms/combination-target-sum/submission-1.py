class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = [] # in a drake voice
        sub = [] # current subset
        N = len(nums)
        def dfs(i, running):
            if running == target:
                combinations.append(sub[:])
                return
            if running > target or i >= N:
                return
            
            # Explicit backtracking
            sub.append(nums[i])
            dfs(i, running + nums[i]) # include
            # Do not include current element
            sub.pop()
            dfs(i+1, running)
        
        dfs(0, 0)
        return combinations


