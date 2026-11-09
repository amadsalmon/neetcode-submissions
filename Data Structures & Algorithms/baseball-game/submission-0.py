class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []

        for op in operations:
            if op == 'C':
                s.pop()
            elif op == 'D':
                s.append(s[-1] * 2)
            elif op == '+':
                a = s.pop()
                b = s.pop()
                s.append(b)
                s.append(a)
                s.append(a + b)
            else:
                s.append(int(op))

        return sum(s)