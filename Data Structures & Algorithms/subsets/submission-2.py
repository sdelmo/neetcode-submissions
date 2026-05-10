class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return []
        subsets = [] # stores final answer
        currsub = [] # stores current subset
        N = len(nums)
        def dfs(i):
            if i >= N:
                subsets.append(currsub[:])
                return
            
            # Include item at i
            currsub.append(nums[i])
            # include next item
            dfs(i+1)
            # do not include item at i
            currsub.pop()
            # include next item
            dfs(i+1)
        
        dfs(0)
        return subsets


