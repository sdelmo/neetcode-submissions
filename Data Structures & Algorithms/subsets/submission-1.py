class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return []

        subsets = [] # Array to store answer
        sub = [] # We keep intermediate/current subset here
        N = len(nums)
        def dfs(i):
            if i >= N:
                subsets.append(sub[:]) # take copy of curr subset
                return
            
            # Two options here
            sub.append(nums[i]) # include element at i
            dfs(i+1) # include next element
            sub.pop()
            dfs(i+1) # do not include element at i
        
        dfs(0)
        return subsets
