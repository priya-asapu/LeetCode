class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"

        result = []

        for word in words:
            w = word.lower()

            count1 = 0
            count2 = 0
            count3 = 0

            for ch in w:
                if ch in row1:
                    count1 += 1
                if ch in row2:
                    count2 += 1
                if ch in row3:
                    count3 += 1

            if count1 == len(w) or count2 == len(w) or count3 == len(w):
                result.append(word)

        return result