class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        combs = []
        curr = []
        N = len(nums)

        running = 0
        def dfs(i, running):
            if running == target:
                combs.append(curr[:])
                return
            if i >= N or running > target:
                return
            
            
            # include branch
            curr.append(nums[i])
            # include same element
            dfs(i,running + nums[i])
            # exclude branch
            curr.pop()
            dfs(i+1,running)
        
        dfs(0, 0)
        return combs

