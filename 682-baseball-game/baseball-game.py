class Solution:
    def calPoints(self, operations: list[str]) -> int:
        scores = []

        for op in operations:
            if op == "C":
                scores.pop()

            elif op == "D":
                last = scores[-1]
                scores.append(last * 2)

            elif op == "+":
                last = scores[-1]
                second = scores[-2]
                scores.append(last + second)

            else:
                number = int(op)
                scores.append(number)

        total = sum(scores)
        return total