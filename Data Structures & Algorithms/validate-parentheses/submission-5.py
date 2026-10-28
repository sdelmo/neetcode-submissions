class Solution:
    def isValid(self, s: str) -> bool:
        matching={
            "}": "{",
            "]": "[",
            ")": "(",
        }
        stack=[]

        for ch in s:
            # Early return, nothing in stack and opening parentheses
            if not stack and ch in matching:
                return False
            elif ch in matching.values():
                stack.append(ch)
            elif ch in matching and stack[-1] == matching[ch]:
                stack.pop()
            else:
                return False
        
        return not stack