# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        # A one element subarray is already sorted
        for i in range(len(pairs)):
            j = i - 1

            while pairs[j].key > pairs[j+1].key and j >= 0:

                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                j -= 1
            res.append(pairs[:])
        return res
            

