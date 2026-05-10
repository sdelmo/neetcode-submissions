# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        def qsort(p,s,e):
            if e - s + 1 <= 1:
                return pairs
            pivot = p[e]
            left = s

            for i in range(s, e):
                if p[i].key < pivot.key:
                    p[i], p[left] = p[left], p[i]
                    left += 1
            
            p[left], p[e] = pivot, p[left]
            qsort(p, s,left-1)
            qsort(p,left+1, e)
        
        qsort(pairs, 0, len(pairs)-1)
        return pairs
        