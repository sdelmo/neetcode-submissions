class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complements = {}

        for i, v in enumerate(nums):

            comp = target - v

            if comp in complements:

                return [complements[comp], i]
            
            else:
                complements[v] = i
        
