class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = [False] * 26

        for ch in s:
            i = ord(ch) - ord('a')
            if seen[i]:
                return ch
            seen[i] = True