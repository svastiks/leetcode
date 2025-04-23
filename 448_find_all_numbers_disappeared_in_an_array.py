class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        """
        Since the original array has duplicates we remove them using a set (set's do. not allow duplicates)

        Time Complexity: O(n)
        Space Complexity: O(n)

        """

        setNums = set(nums)

        new = []

        for i in range(1, len(nums) + 1):
            if i not in setNums:
                new.append(i)

        return new