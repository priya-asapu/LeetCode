class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        count=0
        s=0
        for i in nums:
            count=count+i
        for i in nums:
            if i>9:
                digit=sum(map(int,str(i)))
                s=s+digit
            else:
                s=s+i
        if s>count:
            return (s-count)
        else:
            return (count-s)