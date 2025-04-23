from typing import List

class Solution:

    """
    Optimal Solution:

    We use a hashmap as a key value store, primary data structure

    Time Complexity: O(n)

    Space Complexity: O(n)
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i, v in enumerate(nums):

            diff = target - v

            if diff in hashmap:

                return [hashmap[diff], i]

            hashmap[v] = i              