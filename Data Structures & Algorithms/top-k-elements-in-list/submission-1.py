class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = collections.Counter(nums)
        freq_srted = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
        return [v[0] for v in freq_srted][:k]