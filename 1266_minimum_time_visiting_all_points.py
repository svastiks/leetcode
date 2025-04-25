class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        """
        The distance calculation is Chebyshev distance.

        Time: O(n)
        Space: O(1)

        """

        res = 0
        
        for i in range(len(points) - 1):

            x1, y1 = points[i]
            x2, y2 = points[i+1]

            res += max(abs(x2 - x1), abs(y2 - y1))
        
        return res