# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        
        if len(pairs) <= 1:
            return pairs
        
        def qsort(arr, start, end):
            # unwind
            if end - start + 1 <= 1:
                return
            
            left = start
            pivot = arr[end]

            for i in range(start, end):
                if arr[i].key < pivot.key:
                    arr[left], arr[i] = arr[i], arr[left]
                    left += 1

            arr[left], arr[end] = pivot, arr[left]

            qsort(arr, start, left - 1)
            qsort(arr, left + 1, end)
            return arr

        return qsort(pairs, 0, len(pairs)-1)           
