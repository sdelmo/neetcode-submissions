class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Preprocess the input, just in case we have some empty lists

        matrix = [r for r in matrix if len(r) > 0]

        for row in matrix:

            if row[0] <= target <= row[-1]:

                l, r = 0, len(row) - 1

                while l <= r:

                    mid = (l + r) // 2

                    if row[mid] > target:

                        r = mid - 1
                    
                    elif row[mid] < target:

                        l = mid + 1
                    
                    else:
                        return True
        
        return False
        