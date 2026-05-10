# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def split(a, s, e):
            # one element subarray
            if e - s + 1 <= 1:
                return a
            
            m = (s+e) // 2 # midpoint, where we split

            split(a,s,m)
            split(a,m+1,e)

            merge(a,s,m,e)
            return a
        
        def merge(a,s,m,e):
            i, j, k = 0,0,s


            L = a[s:m+1]
            R = a[m+1:e+1]

            while i < len(L) and j < len(R):

                if L[i].key <= R[j].key:
                    a[k] = L[i]
                    i += 1
                else:
                    a[k] = R[j]
                    j += 1
                k += 1
            
            while i < len(L):
                a[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                a[k] = R[j]
                j += 1
                k += 1
        return split(pairs, 0, len(pairs)-1)
            
