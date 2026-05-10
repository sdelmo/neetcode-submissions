# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        if len(pairs) <= 1:
            return pairs

        def split(iterable, start, end):
            # Divided to a single element arr, unwind
            if end - start + 1 <= 1:
                return

            middle = (end + start) // 2

            # split left half
            split(iterable, start, middle)
            split(iterable, middle + 1, end)

            # merge halves

            merge(iterable, start, middle, end)
            return iterable
        
        def merge(iterable, start, middle, end):

            left = iterable[start:middle+1]
            right = iterable[middle+1:end+1]
            i,j,k = 0, 0, start

            while i < len(left) and j < len(right):

                if left[i].key <= right[j].key:
                    iterable[k] = left[i]
                    i += 1
                else:
                    iterable[k] = right[j]
                    j += 1
                k += 1
            
            while i < len(left):
                iterable[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                iterable[k] = right[j]
                j += 1
                k += 1
        return split(pairs, 0, len(pairs)-1)
