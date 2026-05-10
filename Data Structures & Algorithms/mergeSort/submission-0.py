# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        return self.mSort(pairs, 0, len(pairs)-1)


    def mSort(self, pairs, start, end):

        # Base case, subarray is size 1, return that as it's sorted

        if end - start + 1 <= 1:

            return pairs

        mid = (start + end) // 2

        # Sort left half

        self.mSort(pairs, start, mid)
        self.mSort(pairs, mid + 1, end)

        # Merge subarrays

        self.merge(pairs, start, mid, end)

        return pairs

    def merge(self, pairs, start, mid, end):

        i,j,k = 0,0, start

        L = pairs[start:mid+1]
        R = pairs[mid+1: end+1]

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



        

