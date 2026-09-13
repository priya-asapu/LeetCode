class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        for ch in set(words[0]):
            n = min(word.count(ch) for word in words)
            ans += [ch] * n
        return ans