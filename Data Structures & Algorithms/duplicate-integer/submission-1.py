class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        els = set()

        for n in nums:
            if n in els:
                return True
            else:
                els.add(n)
        
        return False