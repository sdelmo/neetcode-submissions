# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        def qsort(pairs, s, e):

            if e - s + 1 <= 1:
                return pairs

            pivot = pairs[e]
            left = s

            for i in range(s, e):
                if pairs[i].key < pivot.key:
                    pairs[i], pairs[left] = pairs[left], pairs[i]
                    left += 1

            # Move pivot and l
            pairs[e] = pairs[left]
            pairs[left] = pivot

            qsort(pairs, s, left-1)
            qsort(pairs, left+1, e)

        qsort(pairs, 0, len(pairs)-1)
        return pairs
            

        