class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        """
        Time complexity: O(n)
        Space complexity: O(n)
        """

        res = []

        while matrix:

            res += matrix.pop(0)

            if matrix and matrix[0]:
                for r in matrix:
                    res.append(r.pop())

            if matrix:
                res += matrix.pop()[::-1]

            if matrix and matrix[0]:
                for r in matrix[::-1]:
                    res.append(r.pop(0))

        return res
        
