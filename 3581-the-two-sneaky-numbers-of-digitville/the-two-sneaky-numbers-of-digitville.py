class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        l=[]
        s=[]
        for i in nums:
            if i not in l:
                l.append(i)
            else:
                s.append(i)
        return s