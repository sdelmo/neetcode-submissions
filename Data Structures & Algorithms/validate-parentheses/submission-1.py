class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        stack = []

        for ch in s:
            # If closing parenthesis, but nothing in stack, return early, is invalid
            if not stack and ch in matches:
                return False
            # Opening parenthesis
            elif ch in matches.values():
                stack.append(ch)
            # Closing parenthesis
            elif stack and matches[ch] == stack[-1]:
                stack.pop(-1)
            else:
                return False
        
        return not stack
