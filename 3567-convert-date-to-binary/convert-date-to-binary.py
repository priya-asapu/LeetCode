class Solution:
    def convertDateToBinary(self, date: str) -> str:
        l1=date.split("-")
        l2=[]
        for item in l1:
            str2=str(bin(int(item))[2:])
            l2.append(str2)
        return "-".join(l2)