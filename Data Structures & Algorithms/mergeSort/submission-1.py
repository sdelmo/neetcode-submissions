# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        return self.mSort(0, len(pairs)-1, pairs)

    def mSort(self, start, end, arr):

        # Base case, we have a subarray of 1 element
        if end - start + 1 <= 1:
            return arr
        
        mid = (end + start) // 2

        # Break it into two halves, keep going until we have subs of 1

        # Left half
        self.mSort(start, mid, arr)
        self.mSort(mid+1, end, arr)

        self.merge(start, mid, end, pairs)

        return pairs

    def merge(self, start, mid, end, pairs):

        i,j,k = 0,0,start

        L = pairs[start:mid+1]
        R = pairs[mid+1:end+1]

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
        

