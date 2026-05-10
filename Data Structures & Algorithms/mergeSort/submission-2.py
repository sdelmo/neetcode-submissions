# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        return self.split(pairs, 0, len(pairs)-1)
        
    def split(self, pairs, s, e):

        if e - s + 1 <= 1:
            return pairs
        
        mid = (s + e) // 2

        self.split(pairs, s, mid)
        self.split(pairs, mid + 1, e)

        self.merge(pairs, s, mid, e)

        return pairs

    def merge(self, arr, s, mid, e):

        i, j = 0,0
        k = s

        L = arr[s:mid+1]
        R = arr[mid+1:e +1]

        while i < len(L) and j < len(R):

            if L[i].key <= R[j].key:

                arr[k] = L[i]
                i += 1
            
            else:
                arr[k] = R[j]
                j += 1

            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j +=1
            k += 1

        
            
