class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        """
        Since the original array has duplicates we remove them using a set (set's do. not allow duplicates).

        We also check for sets since sets are implemented using hash tables which is way faster for lookups i.e. O(1) time 
        whereas if we do `if i not in nums`, nums here is a List and it will go through the whole list each iteration which is terrible for
        time complexity and will definetly exceed the time limit.

        Time Complexity: O(n)
        Space Complexity: O(n)

        """

        setNums = set(nums)

        new = []

        for i in range(1, len(nums) + 1):
            if i not in setNums:
                new.append(i)

        return new