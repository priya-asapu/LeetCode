class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l=[]
        l1=[]
        for i in nums:
            if i%2==0:
                l.append(i)
            else:
                l1.append(i)
        ans=[]
        for pair in zip(l,l1):
            ans.extend(pair)
        return ans