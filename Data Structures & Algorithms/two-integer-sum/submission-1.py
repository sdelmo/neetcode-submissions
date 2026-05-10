class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        comps = {}

        for i in range(len(nums)):

            remainder = target - nums[i]

            if remainder in comps:
                return [comps[remainder], i]
            
            comps[nums[i]] = i