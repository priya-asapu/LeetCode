class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}

        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        counts = []

        for num in d:
            counts.append(d[num])

        for i in range(len(counts)):
            for j in range(i + 1, len(counts)):
                if counts[i] == counts[j]:
                    return False

        return True