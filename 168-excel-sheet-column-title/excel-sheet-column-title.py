class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            char = chr(remainder + ord('A'))
            result.append(char)
            columnNumber //= 26
            
        return "".join(reversed(result))