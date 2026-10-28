class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        grs = -1

        for i in range(len(arr)-1,-1,-1):
            curr_element = arr[i]
            arr[i] = grs
            grs = max(grs, curr_element)
        
        return arr