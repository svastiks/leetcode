class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        """
        Optimal Solution:

        Time complexity: O(n), iterate through the list and sum

        - Len = O(1)
        - Range object = O(1)
        - Sum = O(n)

        Space complexity: O(1)

        """

        return sum(range(len(nums) + 1)) - sum(nums)

        
        # Brute force, O(nlogn), sorting is slower
        # nums.sort()

        # for i, v in enumerate(nums):

        #     if nums[i] != i:

        #         return i

        #     elif i+1 == len(nums):

        #         return i+1