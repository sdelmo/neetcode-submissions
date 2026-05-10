class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        char_count = {c: s.count(c) for c in s}
        char_count2 = {c: t.count(c) for c in t}

        return True if char_count == char_count2 else False