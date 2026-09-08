class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        distance_value = 0
        
        for num1 in arr1:
            has_close_element = False
            
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    has_close_element = True
                    break  
            if not has_close_element:
                distance_value += 1
                
        return distance_value
