class Solution:
    def completePrime(self, num: int) -> bool:
        def isPrime(n):
            if n < 2:
                return False

            for i in range(2, n):
                if n % i == 0:
                    return False

            return True

        s = str(num)

        
        for i in range(1, len(s) + 1):
            if isPrime(int(s[:i])) == False:
                return False

        
        for i in range(len(s)):
            if isPrime(int(s[i:])) == False:
                return False

        return True