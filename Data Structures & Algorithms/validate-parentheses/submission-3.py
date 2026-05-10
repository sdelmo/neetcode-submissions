class Solution:
    def isValid(self, s: str) -> bool:

        matches = {
            "}": "{",
            ")":"(",
            "]": "[" 
        }

        stack = []

        for ch in s:
            # Edge: Closing par but no opening in stack
            if not stack and ch in matches:
                return False
            elif ch in matches.values():
                stack.append(ch)
            elif ch in matches and matches[ch] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return not stack