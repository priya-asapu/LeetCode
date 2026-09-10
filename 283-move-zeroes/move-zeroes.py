class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=[]
        a=[]
        for i in nums:
            if i!=0:
                l.append(i)
        for i in nums:
            if i==0:
                a.append(i)
        nums[:] = l+a
