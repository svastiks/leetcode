"""
Used a set because it is a data structure that stores unique elements. So no duplicates. 
Lookup, insert, delete is all O(1) in sets
Time complexity: O(n) since it iterates through the list to create the set
Space complexity: size of set
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        setArray = set(nums)

        if(len(setArray) == len(nums)):
            return False
        else:
            return True
        