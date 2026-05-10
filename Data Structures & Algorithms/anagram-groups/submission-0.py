class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict

        ans = defaultdict(list)

        for word in strs:

            ans[tuple(sorted(word))].append(word)

        return ans.values()