class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        ones = 0
        best_one = 0
        for n in nums:
            if n == 1:
                ones += 1
                best_one = max(best_one, ones)
            else:
                ones = 0

        return best_one