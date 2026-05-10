class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for o in operations:
            if o[0] == '-' or o.isdigit():
                scores.append(int(o))
            elif o == '+':
                if len(scores) >= 2:
                    scores.append(scores[-1] + scores[-2])
            elif o == 'D':
                if scores:
                    scores.append(scores[-1]*2)
            elif o == 'C':
                if scores:
                    scores.pop()

        return sum(scores) if scores else 0
