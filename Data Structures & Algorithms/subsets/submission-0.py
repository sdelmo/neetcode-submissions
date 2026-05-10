class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        subsets = [] # where we store our results
        sub = [] # current subset
        N = len(nums)
        def dfs(i):
            if i >= N:
                subsets.append(sub[:])
                return
            
            # Include item at i
            sub.append(nums[i])
            # Include next element, so x0, x1
            dfs(i+1)
            # Skip next element, so x1
            sub.pop()
            dfs(i+1)
        
        dfs(0)
        return subsets
            