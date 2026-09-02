class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        monday_money = 1 
        
        for day in range(n):
            
            total += monday_money + (day % 7)
            
            if (day + 1) % 7 == 0:
                monday_money += 1
                
        return total