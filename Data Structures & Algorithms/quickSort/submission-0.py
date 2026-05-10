# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        
        self.qSort(pairs, 0, len(pairs)-1)

        return pairs

    def qSort(self, pairs, start, end):

        if end - start + 1 <= 1:
            return
        
        pivot = pairs[end]

        left = start

        for i in range(start, end):

            if pairs[i].key < pivot.key:

                pairs[left], pairs[i] = pairs[i], pairs[left]

                left += 1

        pairs[end] = pairs[left]
        pairs[left] = pivot

        self.qSort(pairs, start, left - 1)
        self.qSort(pairs, left + 1, end)