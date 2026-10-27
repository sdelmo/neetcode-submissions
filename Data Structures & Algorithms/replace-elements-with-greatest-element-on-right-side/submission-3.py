class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest = -1
        for i in range(len(arr)-1, -1, -1):
            t = arr[i]
            arr[i] = largest
            largest = max(largest, t)
            
        return arr
