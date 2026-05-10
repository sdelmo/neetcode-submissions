# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)
        res = []

        # iterate from 1 (first element if considered on its own is sorted)

        for i in range(n):
            # Compare to the sorted portion of the array
            j = i - 1

            # Check for bounds
            # Bubble smallest items to the left
            while j >= 0 and pairs[j+1].key < pairs[j].key:
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                j -= 1
            
            # We want the state of array after each insertion
            res.append(pairs[:]) # a copy

        return res  
    