class Solution:
    def addDigits(self, num: int) -> int:
      if num<10:
            return num
      else:

        while num >= 10:
            total = 0

            for i in str(num):
                total = total + int(i)

            num = total

        return num