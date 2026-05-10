class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combs = []
        sub = []
        N = len(nums)
        def dfs(i, csum):
            if csum == target:
                combs.append(sub[:])
                return
            
            if i >= N or csum > target:
                return

            sub.append(nums[i])

            # Include same element
            dfs(i, csum + nums[i])
            sub.pop()
            # Include next element
            dfs(i+1, csum)

        dfs(0, 0)
        return combs

