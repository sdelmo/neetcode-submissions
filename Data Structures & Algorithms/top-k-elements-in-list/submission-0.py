class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ocurrence_hmap = {n: nums.count(n) for n in nums}

        tmp = {k: v for k, v in sorted(ocurrence_hmap.items(), key = lambda item: item[1], reverse = True)}

        keys = list(tmp.keys())
        return keys[:k]