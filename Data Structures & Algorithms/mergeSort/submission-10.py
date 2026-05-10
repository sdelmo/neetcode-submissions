# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        if not pairs:
            return []

        def split(pairs, s, e):
            # Split array to a 1 element subarr
            if e - s + 1 <= 1:
                return
            
            m = (s + e) // 2

            split(pairs, s, m)
            split(pairs, m+1, e)
            merge(pairs, s, m , e)

        def merge(pairs, s,m,e):
            L, R = pairs[s:m+1], pairs[m+1:e+1]
            i,j,k = 0,0,s

            while i < len(L) and j < len(R):

                if L[i].key <= R[j].key:
                    pairs[k] = L[i]
                    i += 1
                
                else:
                    pairs[k] = R[j]
                    j += 1
                k +=1

            while i < len(L):
                pairs[k] = L[i]
                i += 1
                k +=1
            while j < len(R):
                pairs[k] = R[j]
                j +=1
                k +=1

        split(pairs, 0, len(pairs)-1)

        return pairs