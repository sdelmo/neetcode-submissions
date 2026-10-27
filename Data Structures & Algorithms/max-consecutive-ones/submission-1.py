class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive = 0
        best = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                consecutive += 1
            else:
                best = max(best, consecutive)
                consecutive = 0
        
        return max(best, consecutive)