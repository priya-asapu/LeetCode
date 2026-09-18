class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        for length in range(int(area ** 0.5), 0, -1):
            if area % length == 0:
                width = area // length
                return [width, length]