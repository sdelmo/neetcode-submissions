class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        
        from collections import defaultdict
        groups = defaultdict(list)
        
        base = ord("a")
        for word in strs:
            clean_word = word.lower().strip()
            alph = [0] * 26 # Letters in alphabet

            for ch in clean_word:
                idx = ord(ch) - base
                alph[idx] += 1

            groups[tuple(alph)].append(word)
        
        return [g for g in groups.values()]

