class Solution:
  def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
    ans = -1
    dist = float('inf')

    for i, (a, b) in enumerate(points):
        if a == x or b == y:
            d = abs(x-a) + abs(y-b)
            if d < dist:
                dist, ans = d, i

    return ans