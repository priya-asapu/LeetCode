class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for length in range(1, n):
            if n % length == 0:
                substring = s[:length]
                repeated = substring * (n // length)
                if repeated == s:
                    return True
        return False