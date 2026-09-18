class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        result = []
        sorted_scores = sorted(score, reverse=True) 
        for value in score:
            position = sorted_scores.index(value)
            if position == 0:
                result.append("Gold Medal")
            elif position == 1:
                result.append("Silver Medal")
            elif position == 2:
                result.append("Bronze Medal")
            else:
                result.append(str(position + 1))
        return result