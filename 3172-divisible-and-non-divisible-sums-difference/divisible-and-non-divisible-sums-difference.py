class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        l=[]
        l1=[]
        count=0
        s=0
        for i in range(1,n+1):
            if i%m!=0:
                l.append(i)
            else:
                l1.append(i)
        for i in l:
            count=count+i
        for i in l1:
            s=s+i
        return (count-s)