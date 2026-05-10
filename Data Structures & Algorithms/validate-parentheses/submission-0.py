class Solution:
    def isValid(self, s: str) -> bool:
        
        matches = {
            "}" : "{",
            "]" : "[",
            ")" : "("
            }

        stack = []

        for c in s:

            if not stack and c in matches:

                return False
            
            elif c in matches.values():

                stack.append(c)
            
            elif stack and matches[c] == stack[-1]:
                stack.pop(-1)

            else:
                return False

        return True if not stack else False