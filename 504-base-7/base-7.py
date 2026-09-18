class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        negative = False
        if num < 0:
            negative = True
            num = -num
        result = ""
        while num > 0:
            remainder = num % 7
            result = str(remainder) + result
            num = num // 7
        if negative:
            result = "-" + result
        return result