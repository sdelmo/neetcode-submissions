# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        def merge(pairs, s, m, e):
            L = pairs[s:m+1]
            R = pairs[m+1:e+1]

            i,j,k = 0, 0, s

            while i < len(L) and j < len(R):

                if L[i].key <= R[j].key:
                    pairs[k] = L[i]
                    i += 1
                else:
                    pairs[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                pairs[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                pairs[k] = R[j]
                j += 1
                k += 1
            

        # define a helper that splits our subarrays
        def split(pairs, s, e):
            """
            Applies merge sort, this is the top level interface.

            Args:
            pairs: iterable to sort
            int s: Start index for array to sort
            int e: Ending index for array to sort
            """

            # base case, sub array has a size of 1
            # example, e - s + 1 <=1, so 3 - 3 + 1 <= 1 > 1<=1, 1 element
            
            # Travel back up the tree once we reach a element of one, as those are sorted subarrays
            if e - s + 1 <= 1:
                return pairs
            
            # the middle point 
            m = (e + s) // 2

            # sort left half
            split(pairs, s, m)
            
            # sort right half
            split(pairs, m + 1, e)

            # merge the two halves

            merge(pairs, s, m, e)

            return pairs
        
        return split(pairs, 0, len(pairs)-1)
