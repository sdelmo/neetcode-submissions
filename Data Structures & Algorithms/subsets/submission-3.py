class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = []
        currsub = []
        N = len(nums)
        def dfs(i):
            # Base case, computed all subsets starting at i
            if i >= N:
                # take slice copy and return
                subsets.append(currsub[:])
                return
            
            # include element at i
            currsub.append(nums[i])
            # dfs on all subsets including element at i
            dfs(i+1)
            # do not include element at i
            currsub.pop()
            # dfs on all subsets not include element at i
            dfs(i+1)

        dfs(0)
        return subsets
