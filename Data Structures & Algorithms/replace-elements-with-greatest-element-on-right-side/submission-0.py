class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            rval = max(arr[i+1:]) if i + 1 < len(arr) else arr[i]
            arr[i] = rval

        arr[-1] = -1
        return arr
