class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        p = 0
        for i in range(len(arr)):
            arr[p] = max(arr[i+1:]) if (i+1 < len(arr)) else -1
            p += 1
        return arr
            