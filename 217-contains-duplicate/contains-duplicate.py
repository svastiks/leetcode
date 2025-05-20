class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        setArray = set(nums)

        if(len(setArray) == len(nums)):
            return False
        else:
            return True