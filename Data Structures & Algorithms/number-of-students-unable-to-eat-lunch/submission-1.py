from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)
        # count freq of each preference
        cnt = Counter(students) # o(n)

        for s in sandwiches:
            if cnt[s] > 0:
                cnt[s] -= 1
                res -= 1
            else:
                break
        
        return res



